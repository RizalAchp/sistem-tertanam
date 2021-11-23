int  pinLed=6;

void setup() {
  pinMode(pinLed, OUTPUT);         // mensetup pun yang terhubung pada led
}

void loop() {
  digitalWrite(pinLed, HIGH);      // LED pada pin variable hidup
  delay(100);                      // delay selama 0.1 detik
  digitalWrite(pinLed, LOW);       // LED pada pin variable mati 
  delay(100);                      // delay selama 0.1 detik 
}