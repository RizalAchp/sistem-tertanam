/*
  Mengakses pin A2 (Sensor Cahaya LDR)
*/
int pinLDR = A2;
int pinLED = 6;
int nilaiSensor = 0;

void setup() {
  Serial.begin(9600);
  pinMode(pinLDR, INPUT);
  pinMode(pinLED, OUTPUT);
}

void loop() {
  nilaiSensor = analogRead(pinLDR);
  Serial.print(nilaiSensor);
  delay(100);
  if (nilaiSensor >= 700)
  {
    digitalWrite(pinLED, HIGH);
    Serial.println(" tidak mendapat cahaya ");
  }
  else 
  {
    digitalWrite(pinLED, LOW);
    Serial.println(" mendapat cahaya ");
  }
}
