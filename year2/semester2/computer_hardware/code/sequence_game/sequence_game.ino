// sequence_game_4btn.ino
// Arduino/Tinkercad: enter the correct 4-button sequence to win.
// Pins (unchanged):
//   BUTTON1=2, BUTTON2=3, BUTTON3=4, BUTTON4=5, GREEN_LED=6, RED_LED=7, PIEZO=8

const int BUTTON1 = 2;
const int BUTTON2 = 3;
const int BUTTON3 = 4;
const int BUTTON4 = 5;
const int GREEN_LED = 6;
const int RED_LED = 7;
const int PIEZO = 8;

const int correctSequence[] = {BUTTON1, BUTTON3, BUTTON2, BUTTON4};
const int sequenceLength = sizeof(correctSequence) / sizeof(correctSequence[0]);

const unsigned long DEBOUNCE_MS = 30;

int userSequence[sequenceLength];

void setup() {
  pinMode(BUTTON1, INPUT_PULLUP);
  pinMode(BUTTON2, INPUT_PULLUP);
  pinMode(BUTTON3, INPUT_PULLUP);
  pinMode(BUTTON4, INPUT_PULLUP);

  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(PIEZO, OUTPUT);

  digitalWrite(GREEN_LED, LOW);
  digitalWrite(RED_LED, LOW);
}

// ---- Debounced button handling ----
bool isPressed(int pin) {
  return digitalRead(pin) == LOW; // with INPUT_PULLUP, LOW means pressed
}

int readAnyButtonPressed() {
  if (isPressed(BUTTON1)) return BUTTON1;
  if (isPressed(BUTTON2)) return BUTTON2;
  if (isPressed(BUTTON3)) return BUTTON3;
  if (isPressed(BUTTON4)) return BUTTON4;
  return 0;
}

// Waits for a debounced press on any of the 4 buttons, then waits for release.
// Returns the pin of the button pressed.
int waitForButtonPress() {
  // wait for any press
  int candidate = 0;
  while (true) {
    candidate = readAnyButtonPressed();
    if (candidate != 0) {
      // debounce: ensure it's stable for DEBOUNCE_MS
      unsigned long t0 = millis();
      while (millis() - t0 < DEBOUNCE_MS) {
        if (readAnyButtonPressed() != candidate) { candidate = 0; break; }
      }
      if (candidate != 0) break; // stable press confirmed
    }
  }

  // small click feedback (optional)
  tone(PIEZO, 700, 80);

  // wait for release of the same button (also debounced)
  while (isPressed(candidate)) { /* hold */ }
  delay(DEBOUNCE_MS);

  return candidate;
}

// ---- Game helpers ----
bool checkSequence() {
  for (int i = 0; i < sequenceLength; i++) {
    if (userSequence[i] != correctSequence[i]) return false;
  }
  return true;
}

void playWinMelody() {
  int melody[] = {262, 294, 330, 392, 523}; // C D E G C'
  int noteMs = 180;
  for (int i = 0; i < 5; i++) {
    tone(PIEZO, melody[i], noteMs);
    delay(noteMs + 40);
  }
  noTone(PIEZO);
}

void failBlinkAndBeep() {
  for (int i = 0; i < 3; i++) {
    digitalWrite(RED_LED, HIGH);
    tone(PIEZO, 300, 200);
    delay(220);
    digitalWrite(RED_LED, LOW);
    delay(120);
  }
  noTone(PIEZO);
}

void loop() {
  // collect user input
  for (int i = 0; i < sequenceLength; i++) {
    userSequence[i] = waitForButtonPress();
  }

  // evaluate
  if (checkSequence()) {
    digitalWrite(GREEN_LED, HIGH);
    playWinMelody();
    delay(800);
    digitalWrite(GREEN_LED, LOW);
  } else {
    failBlinkAndBeep();
    // quick pause before restart
    delay(500);
  }

  // brief idle indicator between rounds (optional)
  delay(300);
}
