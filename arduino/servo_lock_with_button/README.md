# Servo Lock with Button, LEDs and Buzzer – Arduino/Tinkercad

Electronic lock controlled by a push button. A servo rotates to open/close, LEDs show the state, and the buzzer gives feedback.

## Pins
- Button (to GND, `INPUT_PULLUP`): **7**
- Servo: **2**
- Buzzer: **6**
- Red LED (closed): **10**
- Green LED (open): **11**

## Behavior
- Press button to toggle lock.
- **Open** → servo moves to 90°, green LED ON, 1 short beep.
- **Close** → servo moves back to 0°, red LED ON, 2 short beeps.
- Debounced input ensures reliable button toggling.

## Notes
- In Tinkercad, use a small servo (SG90).
- Adjust servo angles if mechanical limits differ.
- `smoothMove()` makes the servo turn gradually instead of jumping.
