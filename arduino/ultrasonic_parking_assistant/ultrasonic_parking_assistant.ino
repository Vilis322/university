// Arduino/Tinkercad — One-pin ultrasonic distance indicator with toggle button.
//
// Pins (kept exactly as in the original wiring):
//   PING_PIN   = 8   // HC-SR04 style one-pin trigger+echo (Tinkercad-compatible)
//   GREEN_LED  = 9
//   YELLOW_LED = 10
//   RED_LED    = 11
//   BUZZER     = 13
//   BUTTON_PIN = 7   // Toggle system ON/OFF (uses INPUT_PULLUP; pressed = LOW)
//
// Behavior:
//   - Press the button to toggle measuring mode (debounced on press edge).
//   - Distance is measured every ~200 ms using a single pin (trigger then listen).
//   - LEDs indicate zones:  >30 cm = green, 15..30 cm = yellow, <=15 cm = red.
//   - Buzzer beeps faster as you get closer (slow in yellow, fast in red).
//   - When OFF, all outputs are silent/LOW.
//
// Notes:
//   - One-pin mode is fine for Tinkercad. On real hardware prefer separate TRIG/ECHO.
//   - Timeout is handled; if echo not detected, last LED state is cleared to safe (all off).

#define PING_PIN    8
#define GREEN_LED   9
#define YELLOW_LED  10
#define RED_LED     11
#define BUZZER      13
#define BUTTON_PIN  7

// --- thresholds (in cm) ---
const int TH_GREEN  = 30;  // >30 cm → green
const int TH_YELLOW = 15;  // 15..30 cm → yellow; <=15 cm → red

// --- button debounce state ---
bool systemActive = false;
bool lastStable   = HIGH;         // stable level (INPUT_PULLUP: HIGH = released)
bool lastReading  = HIGH;
unsigned long lastDebounceTime = 0;
const unsigned long DEBOUNCE_MS = 50;

// --- measurement pacing ---
unsigned long lastMeasure = 0;
const unsigned long MEASURE_EVERY_MS = 200;

// --- helpers ---
void allOff() {
  digitalWrite(GREEN_LED, LOW);
  digitalWrite(YELLOW_LED, LOW);
  digitalWrite(RED_LED, LOW);
  noTone(BUZZER);
}

long readDistanceCmOnePin() {
  // 1) Trigger: 10 µs HIGH pulse on the same pin
  pinMode(PING_PIN, OUTPUT);
  digitalWrite(PING_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(PING_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(PING_PIN, LOW);

  // 2) Listen: switch to input and measure echo HIGH pulse
  pinMode(PING_PIN, INPUT);
  unsigned long duration = pulseIn(PING_PIN, HIGH, 30000UL); // 30 ms timeout (~>5 m)
  // 3) Return pin to OUTPUT idle LOW (optional, keeps it defined)
  pinMode(PING_PIN, OUTPUT);
  digitalWrite(PING_PIN, LOW);

  if (duration == 0) return -1; // timeout/out of range
  // Distance in cm. Two common forms:
  // return (duration * 0.0343f) / 2.0f;
  return (long)((duration / 2.0f) / 29.1f);
}

void indicateByDistance(long cm) {
  if (cm < 0) {
    // No echo: set safe idle (everything off)
    allOff();
    return;
  }

  if (cm > TH_GREEN) {
    // Far → green, silence
    digitalWrite(GREEN_LED, HIGH);
    digitalWrite(YELLOW_LED, LOW);
    digitalWrite(RED_LED, LOW);
    noTone(BUZZER);
  } else if (cm > TH_YELLOW) {
    // Mid → yellow, slow beep
    digitalWrite(GREEN_LED, LOW);
    digitalWrite(YELLOW_LED, HIGH);
    digitalWrite(RED_LED, LOW);
    tone(BUZZER, 1000, 80);  // short beep
    // No blocking delay here; loop pacing controls repetition rate
  } else {
    // Near → red, fast beep (higher pitch)
    digitalWrite(GREEN_LED, LOW);
    digitalWrite(YELLOW_LED, LOW);
    digitalWrite(RED_LED, HIGH);
    tone(BUZZER, 2000, 80);
  }
}

void setup() {
  pinMode(GREEN_LED, OUTPUT);
  pinMode(YELLOW_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(PING_PIN, OUTPUT);
  digitalWrite(PING_PIN, LOW);

  allOff();
  Serial.begin(9600);
  Serial.println("One-pin ultrasonic: press button to toggle measuring.");
}

void loop() {
  // --- Debounce the toggle button (edge-triggered on press) ---
  bool reading = digitalRead(BUTTON_PIN);
  if (reading != lastReading) {
    lastDebounceTime = millis();
  }
  if ((millis() - lastDebounceTime) > DEBOUNCE_MS) {
    if (reading != lastStable) {
      lastStable = reading;
      if (lastStable == LOW) {
        systemActive = !systemActive;
        // Feedback beeps: 1 for ON, 2 for OFF
        if (systemActive) {
          tone(BUZZER, 1200, 120);
        } else {
          tone(BUZZER, 900, 100); delay(160);
          tone(BUZZER, 900, 100);
          allOff();
        }
      }
    }
  }
  lastReading = reading;

  // --- Periodic measurement when active ---
  if (systemActive && (millis() - lastMeasure >= MEASURE_EVERY_MS)) {
    lastMeasure = millis();
    long cm = readDistanceCmOnePin();
    if (cm < 0) {
      Serial.println("Distance: timeout");
    } else {
      Serial.print("Distance: ");
      Serial.print(cm);
      Serial.println(" cm");
    }
    indicateByDistance(cm);
  }

  // When inactive, ensure outputs are off
  if (!systemActive) {
    allOff();
  }
}
