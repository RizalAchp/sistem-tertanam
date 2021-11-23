int button1     = 2;                // variable pin tombol 1
int pinLed      = 6;                // variable pin LED 
int buttonState = 0;                // variable keadaan tombol 

void setup() {
  pinMode (pinLed, OUTPUT);         // pinLed sebagai output 
  pinMode (button1, INPUT);         // button1 sebagai input
}
void loop() {
  buttonState = digitalRead(button1); // mendeteksi variable keadaan pada tombol
  if (buttonState == LOW){            // ifelse state untuk menentukan keadaan tombol pada LED
    digitalWrite(pinLed, HIGH);
  } else {
    digitalWrite(pinLed, LOW);
  }
}