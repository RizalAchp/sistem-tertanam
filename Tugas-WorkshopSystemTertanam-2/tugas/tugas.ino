/*
 * Menerapkan ide dan gagasan anda untuk membuat project berbasis Arduino Uno, dengan menggunakan 
 * 2 sensor (Sensor jarak SRF04 wajib, satunya pilihan bebas), 2 pushbutton, minimal 2 LED, 1 piezo buzzer, 
 * 1 DC servo dan menerapkan interrupt 
 */
#include <Servo.h>

#define echoPin 11
#define trigPin 12

Servo myServo;

int i;
int r;
int nilaiLDR;
int nilaiPOT;
int durasi;
int jarak;
int p = LOW;
int pinLED[]  = {6,7,8,9};
int pinBuzz = 5;
int button1 = 2;
int button2 = 3;
int pinLDR  = A2;
int pinPOT  = A0;
int waktu   = 500;
boolean sekaliAja=false;

void setup()
{
  Serial.begin(9600);
  for(i = 0; i = 4; i++) {
    pinMode(pinLED[i], OUTPUT);
  }
  pinMode(pinBuzz, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(pinLDR, INPUT);
  pinMode(button2, INPUT);
  myServo.attach(10);
    
  pinMode(button1, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(button1), stopall, CHANGE);
}

void loop() 
{
  if(!sekaliAja)
  {
    sekaliAja=true;
    Serial.println("1. TOMBOL 1 -> Menghentikan semua Loop\n2. TOMBOL 2 -> HCSR04, Servo, dan lain2");
  }
  
  r = digitalRead(button2);
  if(r == HIGH && p == LOW)
  {
    potensio();
    sensorldr();
    ultrasonics();
  }
}

void potensio()
{
  nilaiPOT = analogRead(pinPOT);
  nilaiPOT = map(nilaiPOT, 0, 1023, 0, 180);
  Serial.println(nilaiPOT);
  Serial.print(" ohm |");
  myServo.write(nilaiPOT);
  delay(waktu);
}

void sensorldr()
{
  nilaiLDR = analogRead(pinLDR);
  Serial.print(nilaiLDR);
  delay(waktu);
  
  if(nilaiLDR >=  700) {
    tone(pinBuzz, nilaiLDR);
    Serial.println("-> LDR tidak mendapat cahaya |");
  } 
  else {
    noTone(pinBuzz);
    Serial.println("-> LDR mendapat cahaya |");
  }
}

void ultrasonics()
{
  digitalWrite(trigPin, LOW);
  delay(100);
  digitalWrite(trigPin, HIGH);
  delay(100);
  digitalWrite(trigPin, LOW);
  durasi = pulseIn(echoPin, HIGH);
  jarak = durasi * 0.034 / 2;
  int j = jarak; 
  for(j = 0; j < 100; j++) {
    for(i = 0; i < 4; i++) {
     digitalWrite(pinLED[i], j); 
    }
  }
  
  Serial.print("Jarak : ");
  Serial.print(jarak);
  Serial.println(" Cm");
}

void(* resetFunc) (void) = 0;

void stopall()
{
  resetFunc();
}
