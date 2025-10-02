// seven_segment_button_counter.ino
// Single-digit 7-segment counter with one button.
// - Short press: increment 0..9 (wraps to 0)
// - Long press (>= 1000 ms): reset to 0
// Pins are fixed to the existing wiring:
//   BUTTON_PIN = D3 (INPUT_PULLUP)
//   segmentPins[0..6] = {13,12,11,10,9,8,7}  // segments a..g
//
// Display type:
//   Set COMMON_ANODE = false  -> common cathode (segment ON = HIGH)   [default]
//   Set COMMON_ANODE = true   -> common anode   (segment ON = LOW)
//
// Notes:
//   - Debounce: simple time-based filter.
//   - If your digit wiring order differs, adjust segmentPins order to match a..g.
//   - The bit layout in `numbers[]` is a..g mapped to bits 0..6.

#define BUTTON_PIN 3

// --- Configuration: display polarity ---
const bool COMMON_ANODE = false;  // false = common cathode (ON=HIGH), true = common anode (ON=LOW)

// Segment pins in the order: a, b, c, d, e, f, g
const int segmentPins[7] = {13, 12, 11, 10, 9, 8, 7};

// Segment bitmasks for digits 0..9 (bit0=a ... bit6=g)
const byte numbers[10] = {
  0b00111111,  // 0: a b c d e f
  0b00000110,  // 1:   b c
  0b01011011,  // 2: a b   d e   g
  0b01001111,  // 3: a b c d     g
  0b01100110,  // 4:   b c   f g
  0b01101101,  // 5: a   c d   f g
  0b01111101,  // 6: a   c d e f g
  0b00000111,  // 7: a b c
  0b01111111,  // 8: a b c d e f g
  0b01101111   // 9: a b c d   f g
};

// --- Button/press state ---
int counter = 0;
bool buttonState = HIGH;          // current raw read
bool lastButtonState = HIGH;      // previous raw read
unsigned long lastChangeTime = 0; // last time the raw state changed
const unsigned long debounceMs = 50;

unsigned long pressStartTime = 0; // when the press started
bool longPressHandled = false;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);     // internal pull-up, pressed = LOW
  for (int i = 0; i < 7; i++) {
    pinMode(segmentPins[i], OUTPUT);
  }
  displayNumber(counter);
}

void loop() {
  // --- Debounced button read (pressed = LOW) ---
  bool reading = digitalRead(BUTTON_PIN);

  if (reading != lastButtonState) {
    // edge or bounce detected; start debounce timer
    lastChangeTime = millis();
  }

  // If stable longer than debounce, treat as actual state transition
  if ((millis() - lastChangeTime) > debounceMs && reading != buttonState) {
    buttonState = reading;

    if (buttonState == LOW) {
      // Button pressed
      pressStartTime = millis();
      longPressHandled = false;
    } else {
      // Button released
      unsigned long pressDuration = millis() - pressStartTime;

      // Short press (not long)
      if (!longPressHandled && pressDuration >= 50 && pressDuration < 1000) {
        counter = (counter + 1) % 10;
        displayNumber(counter);
      }
    }
  }

  // Handle long press while the button is held
  if (buttonState == LOW && !longPressHandled) {
    if (millis() - pressStartTime >= 1000) {
      counter = 0;
      displayNumber(counter);
      longPressHandled = true;
    }
  }

  lastButtonState = reading;
}

// --- Display helpers ---

// Writes a raw 7-bit mask (a..g on bits 0..6) to the segment pins, honoring polarity
void writeSegments(byte mask) {
  for (int i = 0; i < 7; i++) {
    bool on = (mask >> i) & 0x01;            // ON for this segment?
    int level = COMMON_ANODE ? !on : on;     // invert if common anode
    digitalWrite(segmentPins[i], level ? HIGH : LOW);
  }
}

// Shows a decimal digit 0..9
void displayNumber(int num) {
  num = num % 10;
  writeSegments(numbers[num]);
}
