# Ultrasonic Distance Toggle (One-Pin HC-SR04) – Arduino/Tinkercad

This project uses a button to toggle an ultrasonic sensor (HC-SR04) measurement mode.  
A buzzer gives feedback: **1 beep = measuring ON**, **2 beeps = measuring OFF**.  
The ultrasonic sensor is wired in **one-pin mode** (TRIG + ECHO on A0).

## Circuit
- **Button**: pin 8 → GND (using `INPUT_PULLUP`)
- **Buzzer**: pin 9 → GND
- **HC-SR04**:
  - VCC → 5V
  - GND → GND
  - TRIG+ECHO → pin A0 (combined, one-pin mode)

## Usage
1. Open `ultrasonic_onepin.ino` in Arduino IDE / Tinkercad and upload.  
2. Open Serial Monitor at **9600 baud**.  
3. Press the button to toggle measuring:
   - ON → one short beep, distances printed every 200 ms  
   - OFF → two short beeps, measuring stops  

## Notes
- Works in Tinkercad with a virtual ultrasonic sensor.  
- Real-world wiring usually requires separate TRIG and ECHO pins.  
- Distance formula: `cm = duration * 0.0344 / 2` (speed of sound ~343 m/s).  
- Timeout = "out of range".
