// Define pins for the button and LEDs
const int buttonPin = 2;     // Button pin
const int led1Pin   = 3;     // First LED pin
const int led2Pin   = 4;     // Second LED pin
const int led3Pin   = 5;     // Third LED pin

// State-tracking variables
int buttonState = 0;         // Current button state
int lastButtonState = 0;     // Previous button state

unsigned long lastPressTime = 0; // Timestamp of last press
unsigned long pressDuration = 0; // Duration of current press

unsigned long lastTapTime = 0;   // Timestamp of last short tap
int tapCount = 0;                // Number of short taps within window
bool waitForDoubleTap = false;   // Flag: waiting for a potential second tap
unsigned long doubleTapStartTime = 0; // Start time of double-tap window

void setup() {
  pinMode(buttonPin, INPUT);     // Button as input (external pull-up/down as wired)
  pinMode(led1Pin, OUTPUT);      // LEDs as outputs
  pinMode(led2Pin, OUTPUT);
  pinMode(led3Pin, OUTPUT);

  digitalWrite(led1Pin, LOW);    // All LEDs off initially
  digitalWrite(led2Pin, LOW);
  digitalWrite(led3Pin, LOW);
}

void loop() {
  // Read current button state
  buttonState = digitalRead(buttonPin);

  // Edge: button pressed (LOW->HIGH depending on wiring; here HIGH means "pressed")
  if (buttonState == HIGH && lastButtonState == LOW) {
    lastPressTime = millis();
    pressDuration = 0;
  }

  // While held: update press duration
  if (buttonState == HIGH && lastButtonState == HIGH) {
    pressDuration = millis() - lastPressTime;
  }

  // Edge: button released
  if (buttonState == LOW && lastButtonState == HIGH) {
    // Short tap (50–300 ms)
    if (pressDuration < 300 && pressDuration > 50) {
      if (millis() - lastTapTime < 500) {
        tapCount++;
      } else {
        tapCount = 1;
      }
      lastTapTime = millis();
      waitForDoubleTap = true;
      doubleTapStartTime = millis();
    }

    // Long press (>= 1000 ms)
    if (pressDuration >= 1000) {
      toggleLED(led2Pin);
      waitForDoubleTap = false; // Cancel double-tap wait
    }
  }

  // If waiting for a double tap and the window (500 ms) elapsed
  if (waitForDoubleTap && millis() - doubleTapStartTime >= 500) {
    if (tapCount == 1) {
      toggleLED(led1Pin);    // Single tap → toggle LED1
    } else if (tapCount == 2) {
      toggleLED(led3Pin);    // Double tap → toggle LED3
    }
    tapCount = 0;
    waitForDoubleTap = false;
  }

  // Save state for the next loop iteration
  lastButtonState = buttonState;
}

// Toggle helper: invert current LED state
void toggleLED(int ledPin) {
  int ledState = digitalRead(ledPin);
  digitalWrite(ledPin, !ledState);
}
