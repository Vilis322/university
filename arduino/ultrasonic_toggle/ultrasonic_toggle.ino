// Button toggles measuring mode, buzzer beeps 1x (on) or 2x (off).
// Uses one pin (A0) as both TRIG and ECHO in Tinkercad.

const int buttonPin = 8;   // button (INPUT_PULLUP)
const int buzzerPin = 9;   // buzzer
const int sensorPin = A0;  // HC-SR04 on one pin (TRIG+ECHO)

bool isActive = false;
bool lastReading = HIGH;
bool stableState = HIGH;
unsigned long lastDebounceTime = 0;
const unsigned long debounceDelay = 50;

void beepOn() {
  tone(buzzerPin, 1000, 200);
}

void beepOff() {
  tone(buzzerPin, 1000, 200);
  delay(200);
  tone(buzzerPin, 1000, 200);
}

long readDistance() {
  // trigger pulse
  pinMode(sensorPin, OUTPUT);
  digitalWrite(sensorPin, LOW);
  delayMicroseconds(2);
  digitalWrite(sensorPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(sensorPin, LOW);

  // switch to input to listen for echo
  pinMode(sensorPin, INPUT);
  long duration = pulseIn(sensorPin, HIGH, 30000); // 30ms timeout
  pinMode(sensorPin, OUTPUT);

  if (duration == 0) return -1; // timeout
  return duration * 0.0344 / 2; // cm
}

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(buzzerPin, OUTPUT);
  pinMode(sensorPin, OUTPUT);
  digitalWrite(sensorPin, LOW);

  Serial.begin(9600);
  Serial.println("Press button to toggle measuring.");
}

void loop() {
  bool reading = digitalRead(buttonPin);

  if (reading != lastReading) {
    lastDebounceTime = millis();
  }
  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != stableState) {
      stableState = reading;
      // Falling edge
      if (stableState == LOW) {
        isActive = !isActive;
        if (isActive) beepOn(); else beepOff();
      }
    }
  }
  lastReading = reading;

  if (isActive) {
    long cm = readDistance();
    if (cm < 0) {
      Serial.println("Distance: out of range / timeout");
    } else {
      Serial.print("Distance: ");
      Serial.print(cm);
      Serial.println(" cm");
    }
    delay(2000);
  }
}