/*
  Mengakses pin A1 (sensor Suhu (LM35) 
*/

int sensorPin = A1;
int nilaiSensor = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int nilaiSensor = analogRead(sensorPin);
  Serial.print(nilaiSensor);
  delay(100);

  float vout = nilaiSensor*(5000/1024.0);
  float temperatur - vout/10;

  Serial.print(" = ");
  Serial.print(temperatur);
  Serial.println("Celcius");
  delay(1000);
}
