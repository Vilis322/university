# Seven-Segment Button Counter – Arduino/Tinkercad

Single-digit 7-segment display controlled by one button:
- **Short press** → increment 0..9 (wraps to 0)
- **Long press (≥ 1000 ms)** → reset to 0

## Pins (kept as in the original wiring)
- **Button:** D3 (using `INPUT_PULLUP`, pressed = LOW)
- **7-segment segments (a..g):** D13, D12, D11, D10, D9, D8, D7

## Display type
The sketch supports both polarities:
- Common cathode (default): segment **ON = HIGH**
- Common anode: set `COMMON_ANODE = true` (segment **ON = LOW**)

## Timing & Debounce
- Debounce: ~50 ms
- Long-press threshold: 1000 ms
- Short-press minimum: 50 ms (ignore micro-taps)

## How it works
- Button uses `INPUT_PULLUP`: the line reads `LOW` when pressed.
- Digit bitmasks (`numbers[]`) map bits 0..6 to segments a..g.
- `displayNumber()` writes the corresponding mask with polarity handling.

## Notes
- Works in Tinkercad or on real hardware (add current-limiting resistors for each segment).
- To invert polarity for **common anode** modules, set `COMMON_ANODE = true`.
