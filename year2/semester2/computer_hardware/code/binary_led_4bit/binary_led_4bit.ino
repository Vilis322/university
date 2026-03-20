// binary_led_4bit.ino
// Shows numbers 0..15 in binary on LEDs at pins 7,6,5,4 (MSB→LSB).

const uint8_t PINS[] = {7, 6, 5, 4};
const size_t NUM_LEDS = sizeof(PINS) / sizeof(PINS[0]);

const unsigned long ERROR_BLINK_MS = 300;
const int ERROR_BLINK_COUNT = 3;

void prompt() {
  Serial.println("Enter a number from 0 to 15:");
}

void clearLeds() {
  for (size_t i = 0; i < NUM_LEDS; ++i) digitalWrite(PINS[i], LOW);
}

void showValue(uint8_t value) {
  for (size_t i = 0; i < NUM_LEDS; ++i) {
    uint8_t bitIndex = (NUM_LEDS - 1) - i;   // MSB→LSB
    bool on = (value >> bitIndex) & 0x01;
    digitalWrite(PINS[i], on ? HIGH : LOW);
  }
}

void blinkError() {
  for (int k = 0; k < ERROR_BLINK_COUNT; ++k) {
    for (size_t i = 0; i < NUM_LEDS; ++i) digitalWrite(PINS[i], HIGH);
    delay(ERROR_BLINK_MS);
    for (size_t i = 0; i < NUM_LEDS; ++i) digitalWrite(PINS[i], LOW);
    delay(ERROR_BLINK_MS);
  }
}

void flushLine() {
  while (Serial.available()) { if (Serial.read() == '\n') break; }
}

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);
  for (size_t i = 0; i < NUM_LEDS; ++i) pinMode(PINS[i], OUTPUT);
  clearLeds();
  prompt();
}

void loop() {
  if (Serial.available() > 0) {
    long value = Serial.parseInt();
    flushLine();

    Serial.print("You entered: ");
    Serial.println(value);

    if (value >= 0 && value < (1 << NUM_LEDS)) {
      showValue((uint8_t)value);
    } else {
      blinkError();
      clearLeds();
    }
    prompt();
  }
}