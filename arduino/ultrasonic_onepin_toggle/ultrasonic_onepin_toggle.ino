//   trigEchoPin = 7  (TRIG+ECHO on one pin, Tinkercad-style)
//   buttonPin   = 8  (INPUT_PULLUP)
//   buzzerPin   = 6
//
// Behavior:
//   - Press button to toggle measuring (debounced on press edge).
//   - ON  -> 1 beep; prints distance every ~250 ms
//   - OFF -> 2 beeps.
//   - Timeout is handled (no hangs).

const int trigEchoPin = 7;
const int buttonPin   = 8;    // to GND, INPUT_PULLUP
const int buzzerPin   = 6;

bool systemActive = false;

// Debounce state
bool lastStable = HIGH;        // with INPUT_PULLUP, HIGH = released
bool lastReading = HIGH;
unsigned long lastDebounceTime = 0;
const unsigned long debounceDelay = 50; // ms

// Measure pacing
unsigned long lastMeasure = 0;
const unsigned long measureEveryMs = 250; // ms

void beep(int times) {
  const int f = 1000;
  for (int i = 0; i < times; i++) {
    tone(buzzerPin, f, 180);
    delay(220);
  }
}

long readDistanceCm() {
  // Trigger 10us pulse
  pinMode(trigEchoPin, OUTPUT);
  digitalWrite(trigEchoPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigEchoPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigEchoPin, LOW);

  // Listen for echo on the same pin
  pinMode(trigEchoPin, INPUT);
  unsigned long duration = pulseIn(trigEchoPin, HIGH, 30000UL); // 30 ms timeout
  pinMode(trigEchoPin, OUTPUT);  // return to OUTPUT idle
  digitalWrite(trigEchoPin, LOW);

  if (duration == 0) return -1;  // timeout
  // Two equivalent formulas:
  // return (duration * 0.0343f) / 2.0f;     // using 0.0343 cm/us
  return (duration / 2.0f) / 29.1f;          // using 1/29.1 cm/us (~343 m/s)
}

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(buzzerPin, OUTPUT);
  pinMode(trigEchoPin, OUTPUT);
  digitalWrite(trigEchoPin, LOW);

  Serial.begin(9600);
  Serial.println("Press button to toggle measuring.");
}

void loop() {
  // --- Debounce (edge-triggered) ---
  bool reading = digitalRead(buttonPin);
  if (reading != lastReading) {
    lastDebounceTime = millis();
  }
  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != lastStable) {
      lastStable = reading;
      // Falling edge: button pressed
      if (lastStable == LOW) {
        systemActive = !systemActive;
        if (systemActive) beep(1); else beep(2);
      }
    }
  }
  lastReading = reading;

  // --- Measuring loop (non-blocking) ---
  if (systemActive && (millis() - lastMeasure >= measureEveryMs)) {
    lastMeasure = millis();
    long cm = readDistanceCm();
    if (cm < 0) {
      Serial.println("Distance: timeout");
    } else {
      Serial.print("Distance: ");
      Serial.print(cm);
      Serial.println(" cm");
    }
  }
}
