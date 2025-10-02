// Arduino/Tinkercad: send words in Morse code on LED at pin 13.
// Demonstration sends "SOS" using sendWord("SOS").
//
// Morse timing (ITU):
// dot = 1 unit ON
// dash = 3 units ON
// gap between symbols (inside a letter) = 1 unit OFF
// gap between letters = 3 units OFF
// gap between words   = 7 units OFF
//
// How it’s structured:
// - dot()/dash()  → emit a symbol with correct intra-letter gap
// - codeFor(ch)   → returns Morse string for 'A'..'Z' and '0'..'9' ("" if unsupported)
// - sendLetter(ch, lastInWord) → emits one letter and then 3u gap (or 7u if it's the last in word)
// - sendWord("TEXT") → walks through characters, skips spaces, handles last-letter-in-word logic

const int LED_PIN = 13;
const int UNIT_MS = 120;  // tweak speed

// Morse tables: A..Z (index = letter - 'A'), 0..9 (index = digit - '0')
const char* MORSE_AZ[26] = {
  ".-",   "-...", "-.-.", "-..",  ".",    "..-.", "--.",  "....", "..",    // A-I
  ".---", "-.-",  ".-..", "--",   "-.",   "---",  ".--.", "--.-", ".-.",   // J-R
  "...",  "-",    "..-",  "...-", ".--",  "-..-", "-.--", "--.."           // S-Z
};
const char* MORSE_09[10] = {
  "-----", ".----", "..---", "...--", "....-",  // 0-4
  ".....", "-....", "--...", "---..", "----."   // 5-9
};

void ledOn(int ms) {
  digitalWrite(LED_PIN, HIGH);
  delay(ms);
  digitalWrite(LED_PIN, LOW);
}

// Emit a dot; add intra-letter 1u gap unless it's the last symbol of the letter
void dot(bool lastInLetter) {
  ledOn(UNIT_MS);
  if (!lastInLetter) delay(UNIT_MS);
}

// Emit a dash; add intra-letter 1u gap unless it's the last symbol of the letter
void dash(bool lastInLetter) {
  ledOn(3 * UNIT_MS);
  if (!lastInLetter) delay(UNIT_MS);
}

// Uppercase conversion without <ctype.h>
char toUpperFast(char c) {
  if (c >= 'a' && c <= 'z') return c - ('a' - 'A');
  return c;
}

// Return Morse code string for supported characters, or "" if unsupported.
const char* codeFor(char c) {
  c = toUpperFast(c);
  if (c >= 'A' && c <= 'Z') return MORSE_AZ[c - 'A'];
  if (c >= '0' && c <= '9') return MORSE_09[c - '0'];
  return ""; // unsupported (punctuation etc.)
}

// Emit a single letter in Morse (handles symbol gaps internally).
// After the letter, wait 3u (letter gap) or 7u (word gap if lastInWord = true).
void sendLetter(char letter, bool lastInWord) {
  const char* code = codeFor(letter);
  if (*code == '\0') {
    // unsupported char just skip with a letter gap to keep rhythm
    delay(3 * UNIT_MS);
    return;
  }

  // Walk over symbols in the code
  int len = 0;
  while (code[len] != '\0') len++;

  for (int i = 0; i < len; ++i) {
    bool lastSymbol = (i == len - 1);
    char s = code[i];
    if (s == '.')      dot(lastSymbol);
    else /* s == '-' */ dash(lastSymbol);
  }

  // Inter-letter / word gap
  if (lastInWord) delay(7 * UNIT_MS);
  else            delay(3 * UNIT_MS);
}

// Emit a whole word (letters separated by 3u, words by 7u).
// Spaces in the input add a word gap and do not emit a letter.
void sendWord(const char* word) {
  // Compute the count of letters that will actually be emitted (non-spaces)
  int totalLetters = 0;
  for (int i = 0; word[i] != '\0'; ++i) {
    if (word[i] != ' ') totalLetters++;
  }
  if (totalLetters == 0) {
    delay(7 * UNIT_MS);
    return;
  }

  int emitted = 0;
  for (int i = 0; word[i] != '\0'; ++i) {
    char c = word[i];
    if (c == ' ') {
      // explicit space: ensure a full word gap (7u)
      delay(7 * UNIT_MS);
      continue;
    }
    emitted++;
    bool lastInWord = (emitted == totalLetters);
    sendLetter(c, lastInWord);
  }
}

void setup() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
}

void loop() {
  // Demo: send "SOS", then pause a bit and repeat
  sendWord("SOS");
  delay(7 * UNIT_MS); // extra pause between repetitions (word gap)
}