int pinLed=6;

void setup() {
  pinMode(pinLed, OUTPUT);
  Serial.begin(9600);
  Serial.println("Input 1 = LED Menyala, Input 2 = LED padam");
}
void loop() {
  if(Serial.available()) {
    int kondisi=Serial.parseInt();
    if(kondisi==1) {
      digitalWrite(pinLed,HIGH);
      Serial.println("LED MENYALA");
    }
    if(kondisi==2) {
      digitalWrite(pinLed,LOW);
      Serial.println("LED PADAM");
    }
  }
}