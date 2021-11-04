/*
  Mengakses pin 10 sebagai actuator DC servo
 */

#include <Servo.h>

Servo servo1;;
int pos = 0;

void setup() {
  servo1.attach(10);
}

void loop() {
  for(pos = 0; pos <= 180; pos += 1)
  {
    servo1.write(pos);
    delay(15);
  }
  for(pos = 180; pos >= 0; pos -= 1)
  {
    servo1.write(pos);
    delay(15);
  }
}
