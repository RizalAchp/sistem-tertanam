/*
 Mengakses pin 0 (variable resistor dan LED)
*/
int pinSensor = A0;
int pinLed = 6;
int nilaiSensor = 0;

void setup() {
  Serial.begin(9600);
  pinMode(pinLed),OUTPUT);
}

void loop() {
  nilaiSensor = analogRead(pinSensor);
  Serial.println(nilaiSensor);
  digitalWrite(pinLed, HIGH);
  delay(nilaiSensor);
  digitalWrite(pinLed, LOW);
  delay(nilaiSensor);
}
