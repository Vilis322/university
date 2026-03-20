# 4-Button Sequence Game – Arduino/Tinkercad

Press four buttons in the correct order to win. Success lights the green LED and plays a short melody; failure blinks the red LED with error beeps, then the round restarts.

## Pins
- **Buttons (to GND with INPUT_PULLUP):** 2, 3, 4, 5
- **Green LED:** 6
- **Red LED:** 7
- **Piezo/Buzzer:** 8

## How it works
- The correct sequence is `{2, 4, 3, 5}` in this example (B1, B3, B2, B4 by pin mapping).
- Button reads are **debounced** and require **release** before the next input.
- On success: green LED + melody.  
- On failure: red LED blinks + error beeps, then a new round starts automatically.

## Notes
- Pull-up logic: a pressed button reads **LOW**.
- Adjust `DEBOUNCE_MS` if your buttons are noisy.
- Change `correctSequence[]` to set a new target combination.
