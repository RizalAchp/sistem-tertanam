/*
 Mengakses pin 10 sebagai DC Servo dan Variable Resist
 */
#include <Servo.h>

Servo servo1;
int pot = A0;
int nilaiSensor;

void setup() {
  servo1.attach(10);
}

void loop() {
  nilaiSensor = analogRead(pot);
  nilaiSensor = map(nilaiSensor, 0, 1023, 0, 180);
  servo1.write(nilaiSensor);
  delay(15);
}
