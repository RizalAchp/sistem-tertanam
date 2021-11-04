int pinLed=6;

void setup() {
  pinMode(pinLed, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(pinLed,HIGH);
  Serial.println("LED MENYALA");
  delay(100);
  digitalWrite(pinLed,LOW);
  Serial.println("LED PADAM");
  delay(100);
}