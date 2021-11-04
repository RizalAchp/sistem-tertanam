/*
 * interrupt (3)
 */

int pinLed1 = 9;
int pinLed2 = 8;
int pinLed3 = 7;
int pinLed4 = 6;

void setup() {
  pinMode(pinLed1, OUTPUT);
  pinMode(pinLed2, OUTPUT);
  pinMode(pinLed3, OUTPUT);
  pinMode(pinLed4, OUTPUT);
  pinMode(2, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(2),fungsiInt, FALLING);
}

void fungsiInt()
{
  digitalWrite(pinLed2, LOW);
  delay(5000);
}

void loop() {
  digitalWrite(pinLed1, HIGH);
  delay(1000);
  digitalWrite(pinLed2, HIGH);
  delay(1000);
  digitalWrite(pinLed3, HIGH);
  delay(1000);
  digitalWrite(pinLed4, HIGH);
  delay(1000);
}
