const int trigPin = 2;
const int echoPin = 3;
const int LEDlampRed = 4;
const int LEDlampYellow = 5;
const int LEDlampGreen = 6;
const int buzzer = 7;
int sound = 500;

void setup() {
Serial.begin (9600);
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
pinMode(LEDlampRed, OUTPUT);
pinMode(LEDlampYellow, OUTPUT);
pinMode(LEDlampGreen, OUTPUT);
pinMode(buzzer, OUTPUT);
}
void loop() {
long durationindigit, distanceincm;
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
durationindigit = pulseIn(echoPin, HIGH);
distanceincm = (durationindigit * 0.034) / 2;

if (distanceincm > 50) {
digitalWrite(LEDlampGreen, LOW);
digitalWrite(LEDlampYellow, LOW);
digitalWrite(LEDlampRed, LOW);
noTone(buzzer);
}
else if (distanceincm <= 50 && distanceincm > 20) {
digitalWrite(LEDlampGreen, HIGH);
digitalWrite(LEDlampYellow, LOW);
digitalWrite(LEDlampRed, LOW);
noTone(buzzer);
}
else if (distanceincm <= 20 && distanceincm > 5) {
digitalWrite(LEDlampYellow, HIGH);
digitalWrite(LEDlampGreen, HIGH);
digitalWrite(LEDlampRed, LOW);
tone(buzzer, 500);
}
else if (distanceincm <= 0) {
digitalWrite(LEDlampGreen, LOW);
digitalWrite(LEDlampYellow, HIGH);
digitalWrite(LEDlampRed, LOW);
noTone(buzzer);
}
else {
digitalWrite(LEDlampGreen, HIGH);
digitalWrite(LEDlampYellow, HIGH);
tone(buzzer, 1000);
digitalWrite(LEDlampRed, HIGH);
delay(300);
digitalWrite(LEDlampRed, LOW);
}

Serial.print(distanceincm);
Serial.println(" cm");

delay(300);
}
