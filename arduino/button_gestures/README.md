# Button Gestures for 3 LEDs – Arduino/Tinkercad

Control three LEDs using a single button with gesture-like inputs:
- **Single tap (50–300 ms)** → toggle LED1
- **Double tap** (two short taps within 500 ms) → toggle LED3
- **Long press (≥ 1000 ms)** → toggle LED2

## Pins
- **Button:** pin 2 (configured as `INPUT`; use an external pull-up/down as wired)
- **LED1:** pin 3
- **LED2:** pin 4
- **LED3:** pin 5

## Timing
- Short tap window: **50–300 ms**
- Double-tap detection window: **500 ms** after the first tap
- Long press threshold: **1000 ms**

## Behavior
- On release, short taps are counted to detect single vs double tap.
- Long press toggles LED2 and cancels any pending double-tap wait.

## Notes
- If you wire the button to GND and prefer internal pull-up, change to `pinMode(buttonPin, INPUT_PULLUP)` and invert logic accordingly.
- LED pins are driven as simple digital outputs (active HIGH).
