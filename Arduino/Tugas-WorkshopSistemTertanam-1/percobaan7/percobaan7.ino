int pinLed=6;
void setup() {
  pinMode(pinLed, OUTPUT) ;
}
void loop() {
  digitalWrite(pinLed, 255);
  delay(100);
  digitalWrite(pinLed, 128);
  delay(100);
  digitalWrite(pinLed, 0);
  delay(100);
}