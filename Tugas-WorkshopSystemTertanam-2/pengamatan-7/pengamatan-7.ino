/*
 Mengakses pin 11 dan 12 sebagai Sensor Jaran SRF04
 */

#define echoPin 11
#define trigPin 12

long durasi;
int jarak;

void setup() {
  Serial.begin(9600);
  pinMode(echoPin, INPUT);
  pinMode(trigPin, OUTPUT);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delay(100);
  digitalWrite(trigPin, HIGH);
  delay(100);
  digitalWrite(trigPin, LOW);
  durasi = pulseIn(echoPin, HIGH);
  jarak = durasi * 0.034 / 2;
  Serial.print("Jarak : ");
  Serial.print(jarak);
  Serial.println(" Cm");
}
