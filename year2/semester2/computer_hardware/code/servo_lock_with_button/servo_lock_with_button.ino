#include <Servo.h>

// --- Pin definitions ---
const int buttonPin    = 7;   // Push button (to GND, INPUT_PULLUP)
const int redLEDPin    = 10;  // Red LED = locked
const int greenLEDPin  = 11;  // Green LED = unlocked
const int buzzerPin    = 6;   // Piezo buzzer
const int servoPin     = 2;   // Servo control pin

// --- Objects and state ---
Servo lockServo;
bool isOpen = false;             // Current state of the lock
bool lastButtonState = HIGH;     // Previous button state
unsigned long lastDebounceTime = 0;
const int debounceDelay = 50;    // Debounce time in ms

void setup() {
  // Configure pins
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(redLEDPin, OUTPUT);
  pinMode(greenLEDPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);

  // Attach servo and set initial position (locked)
  lockServo.attach(servoPin);
  lockServo.write(0);

  // Initial LED state: locked
  digitalWrite(redLEDPin, HIGH);
  digitalWrite(greenLEDPin, LOW);
}

void loop() {
  // Read button state
  bool buttonState = digitalRead(buttonPin);

  // Detect button press (HIGH -> LOW) with debounce
  if (buttonState == LOW && lastButtonState == HIGH && (millis() - lastDebounceTime) > debounceDelay) {
    lastDebounceTime = millis();
    isOpen = !isOpen;   // Toggle lock state

    if (isOpen) {
      beep(1);                     // Single beep for unlock
      smoothMove(0, 90);           // Rotate servo to 90° smoothly
      digitalWrite(redLEDPin, LOW);
      digitalWrite(greenLEDPin, HIGH);
    } else {
      beep(2);                     // Double beep for lock
      smoothMove(90, 0);           // Rotate servo back to 0° smoothly
      digitalWrite(redLEDPin, HIGH);
      digitalWrite(greenLEDPin, LOW);
    }
  }

  // Save button state for next loop
  lastButtonState = buttonState;
}

// --- Helper functions ---

// Smoothly move servo from start to end angle
void smoothMove(int startAngle, int endAngle) {
  if (startAngle < endAngle) {
    for (int pos = startAngle; pos <= endAngle; pos++) {
      lockServo.write(pos);
      delay(15); // adjust for speed
    }
  } else {
    for (int pos = startAngle; pos >= endAngle; pos--) {
      lockServo.write(pos);
      delay(15);
    }
  }
}

// Generate short beeps: once for unlock, twice for lock
void beep(int times) {
  for (int i = 0; i < times; i++) {
    tone(buzzerPin, 1000, 150);
    delay(250);
  }
}
