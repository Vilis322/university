# Ultrasonic Toggle (One-Pin) – Arduino/Tinkercad

Toggle HC-SR04 measuring with a debounced button. Works in Tinkercad with TRIG+ECHO combined on a single pin.

## Pins
- TRIG+ECHO: **7**
- Button (to GND, `INPUT_PULLUP`): **8**
- Buzzer: **6**

## Behavior
- Press button to toggle measuring.
- ON → 1 beep, distances printed every ~250 ms.
- OFF → 2 beeps.
- Timeouts are handled (no freezing).

## Notes
- One-pin mode is fine for Tinkercad; in real hardware prefer separate TRIG/ECHO.
- Distance formula uses speed of sound ≈ 343 m/s.
