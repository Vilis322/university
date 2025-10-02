int dot = 100;
int dash = 300;
int between_messages = 400;

void setup() {
pinMode(13, OUTPUT);
}

void loop() {
digitalWrite(13, HIGH);
delay(dot);
digitalWrite(13, LOW);
delay(dot);
digitalWrite(13, HIGH);
delay(dot);
digitalWrite(13, LOW);
delay(dot);
digitalWrite(13, HIGH);
delay(dot);
digitalWrite(13, LOW);
delay(dot);
delay(dot);
digitalWrite(13, HIGH);
delay(dash);
digitalWrite(13, LOW);
delay(dash);
digitalWrite(13, HIGH);
delay(dash);
digitalWrite(13, LOW);
delay(dash);digitalWrite(13, HIGH);
delay(dash);
digitalWrite(13, LOW);
delay(dash);
delay(dot);
digitalWrite(13, HIGH);
delay(dot);
digitalWrite(13, LOW);
delay(dot);
digitalWrite(13, HIGH);
delay(dot);
digitalWrite(13, LOW);
delay(dot);
digitalWrite(13, HIGH);
delay(dot);
digitalWrite(13, LOW);
delay(dot);
delay(between_messages);
}