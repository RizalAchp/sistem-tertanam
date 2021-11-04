/*
  pin 10 dihubungkan dengan piezo buzzer
  func loop setiap 0.1 detik.
*/
void setup() {
  pinMode(10, OUTPUT);
}

void loop() {
  digitalWrite(10, HIGH);
  delay(100);
  digitalWrite(10, LOW);
  delay(100);
}
