void setup() {
  pinMode(6, OUTPUT);         // mensetup pun yang terhubung pada led
}

void loop() {
  digitalWrite(6, HIGH);      // LED pada pin 6 hidup
  delay(100);                 // delay selama 0.1 detik
  digitalWrite(6, LOW);       // LED pada pin 6 mati 
  delay(100);                 // delay selama 0.1 detik 
}