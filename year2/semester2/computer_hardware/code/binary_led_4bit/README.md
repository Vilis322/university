# Binary LED (4-bit) – Arduino/Tinkercad

Displays a number (0–15) as a 4-bit binary value on four LEDs connected to pins 7, 6, 5, 4.  
If the input is out of range, all LEDs blink three times.

## Circuit
- 4× LEDs with ~220Ω resistors in series  
- Pins: **7, 6, 5, 4** → LED outputs  
- Common GND to Arduino GND

## How to use
1. Open `binary_led_4bit.ino` in Arduino IDE and upload.  
2. Open Serial Monitor at **9600 baud**.  
3. Enter an integer **0..15** → LEDs show its binary (MSB on pin 7, LSB on pin 4).  
4. Any other value → all LEDs blink 3 times.