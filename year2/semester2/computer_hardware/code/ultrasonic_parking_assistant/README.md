# Ultrasonic Parking Assistant (One-Pin) – Arduino/Tinkercad

Distance indicator using a single-pin ultrasonic setup (trigger + echo on the same pin).
A button toggles the system ON/OFF; LEDs show range zones and the buzzer beeps faster as you get closer.

## Pins (as wired)
- **Ultrasonic (one-pin TRIG+ECHO):** D8
- **Green LED:** D9
- **Yellow LED:** D10
- **Red LED:** D11
- **Buzzer:** D13
- **Button (toggle, to GND with `INPUT_PULLUP`):** D7

## Behavior
- Press the button to toggle measuring mode.
- Measurements update about every **200 ms**.
- **> 30 cm** → Green ON, buzzer off  
- **15–30 cm** → Yellow ON, slow beeps (~1000 Hz)  
- **≤ 15 cm** → Red ON, faster beeps (~2000 Hz)
- If echo times out, all outputs go off (safe idle).
- ON feedback: 1 beep; OFF feedback: 2 short beeps.

## Tinkercad Notes
- One-pin mode works in Tinkercad virtual HC-SR04.
- On real hardware, prefer separate TRIG/ECHO pins for robustness.
- The sketch uses `pulseIn(..., 30000)` to avoid long blocking if no echo is received.

## Tuning
- Change thresholds in code: `TH_GREEN` and `TH_YELLOW`.
- Adjust pacing via `MEASURE_EVERY_MS`.
- Beep tones/durations can be customized in `indicateByDistance()`.

## Troubleshooting
- **Always timeout**: check D8 wiring and ground; ensure an object is in front of the sensor (10–50 cm).
- **No beeps**: verify the buzzer polarity and pin D13.
- **Button not toggling**: confirm D7 is wired to GND and `INPUT_PULLUP` is used.
