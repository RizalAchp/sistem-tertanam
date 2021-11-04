/*
 * Menerapkan ide dan gagasan untuk membuat project berbasis Arduino Uno, dengan menggunakan 
 * 2 sensor (Sensor jarak SRF04 wajib, satunya pilihan bebas), 2 pushbtn, minimal 2 LED, 1 piezo buzzer, 
 * 1 DC servo dan menerapkan interrupt 
 */

#include <Servo.h>

#define echoPin 11
#define trigPin 12

Servo myServo;

int pinLed1     = 6;
int pinLed2     = 7;
int pinLed3     = 8;
int pinLed4     = 9;
int pinBuzz     = 5;
int btn1        = 2;
int btn2        = 3;
int btn3        = 4;
int ldrPin      = A0;
int pinServ     = 10;
int posBtn2, lastBtn2, kon2=0; int posBtn3, lastBtn3, kon3=0;
int dur; int jarCm = 0; int lr; int suara; int sudut;

void setup()
{
    pinMode(pinLed1, OUTPUT);
    pinMode(pinLed2, OUTPUT);
    pinMode(pinLed3, OUTPUT);
    pinMode(pinLed4, OUTPUT);
    pinMode(pinBuzz, OUTPUT);
    pinMode(ldrPin, INPUT);
    pinMode(echoPin, INPUT);
    pinMode(trigPin, OUTPUT);

    myServo.attach(pinServ);

    pinMode(btn1, INPUT_PULLUP);
    pinMode(btn2, INPUT_PULLUP);
    pinMode(btn3, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(btn1), funcInt, RISING);
    
    Serial.begin(9600);
    Serial.println("1)TOMBOL 1-> Intterupt button\n2)TOMBOL 2 -> Fungsi semua loop\n3) TOMBOL 3 -> Menstop Loop");
}

void loop() // memakai void baru untuk fungsi yang berbeda sesuai switch yang di  tekan.
{
    posBtn2 = digitalRead(btn2);
    posBtn3 = digitalRead(btn3);
    if ((posBtn2 == LOW) && (lastBtn2 == HIGH)) {
        kon2 = 1 - kon2;
        delay(10);
    }
    lastBtn2 = posBtn2;
    if ((posBtn3 == LOW) && (lastBtn3 == HIGH)) {
        kon3 = 1 - kon3;
        delay(10);
    }
    lastBtn3 = posBtn3;

    if(kon2 == 1) {
        button_dua();
    } else {
        noTone(pinBuzz);
    }
        
    if(kon3 == 1) {
        button_tiga();
    } else {
        noTone(pinBuzz);
    }
}
    
void button_dua() {
    /* saat switch 2 di tekan, maka led akan hidup sesuai
     * nilai bacaan pada ultrasonic sensor.
     * dan saat bacaan yang didapat melebihi nilai yang ditentukan,
     * maka buzzer akan berbunyi
     */
    digitalWrite(trigPin, LOW);
    delay(100);
    digitalWrite(trigPin, HIGH); 
    delay(100);
    digitalWrite(trigPin, LOW); 
    dur = pulseIn(echoPin, HIGH);
    jarCm = dur * 0.034 / 5;
    Serial.print("Jarak yang di Baca : ");
    Serial.println(jarCm);
    Serial.println("===================");

    if(jarCm >= 10) {
        digitalWrite(pinLed1, HIGH);
        delay(100);
    }
    if(jarCm >= 50) {
        digitalWrite(pinLed2, HIGH);
        delay(100);
    }
    if(jarCm >= 75) {
        digitalWrite(pinLed3, HIGH);
        delay(100);
    }
    if(jarCm >= 100) { 
        digitalWrite(pinLed4, HIGH);
        tone(pinBuzz, 900);
        delay(100);
    } else
        noTone(pinBuzz);
        digitalWrite(pinLed1, LOW);
        digitalWrite(pinLed2, LOW);
        digitalWrite(pinLed3, LOW);
        digitalWrite(pinLed4, LOW);
}

void button_tiga()
{
    /* saat switch 3 ditekan, maka arduino akan membaca masukan
     * nilai sensor ldr, dan menjadikannya sebagai nilai tone buzzer
     * dan gerkan servo.
     */
    lr = analogRead(ldrPin);
    delay(500);
    suara = lr + 500;
    Serial.print("TUne yang didapat dari Cahaya = ");
    Serial.println(suara);
    Serial.println("============");
    tone(pinBuzz, suara);
    delay(500);
    sudut = map(lr, 0, 1023, 0, 180);
    myServo.write(sudut);
    Serial.print("Sudut servo = ");
    Serial.println(sudut);
}

void funcInt() {
    tone(pinBuzz, 900);
    delay(5000);
}
