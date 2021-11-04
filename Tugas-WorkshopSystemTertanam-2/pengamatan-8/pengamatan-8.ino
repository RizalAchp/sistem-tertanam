/*
 interupt 
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
}

void loop() {
  digitalWrite(pinLed1, HIGH);
  delay(100);
  digitalWrite(pinLed2, HIGH);
  delay(100);
  digitalWrite(pinLed3, HIGH);
  delay(100);
  digitalWrite(pinLed4, HIGH);
  delay(100);

  if (diitalRead(2) == LOW)
  {
    digitalWrite(pinLed2, LOW);
    delay(10000);
  }
}
