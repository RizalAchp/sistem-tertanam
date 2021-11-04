/* 
Mengakses pin A0(analog 0) dengan 
variable resistor / potensio 
*/

void setup() {
  Serial.begin(9600);
}

void loop() {
  int nilaiSensor = analogRead(A0);
  Serial.println(nilaiSensor);
  delay(100);  
}
