/*-----------------------------------------------------
'     
'     TRIG --> Pin 7
'     ECHO --> Pin 6
'     Baud Rate 9600 bps
'     Ogi sinatra
'     AT-MO PRODUCTION
'-----------------------------------------------------*/


//pin Ultrasonik
#define trigPin 7
#define echoPin 6

#define ledAman 8
#define led1 9
#define led2 10
#define led3 11



void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
 
  pinMode(ledAman, OUTPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
 
}

void loop() {
  long duration, distance;
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2) / 29.1;
 

  if (distance >= 50) 
  {
    digitalWrite(ledAman, HIGH);
      digitalWrite(led1, LOW);
      digitalWrite(led2, LOW);
      digitalWrite(led3,LOW);
  }
  else {
    digitalWrite(ledAman,LOW);
  }
  
  if (distance <= 100) 
  {
      digitalWrite(led1, HIGH);
      digitalWrite(led2, LOW);
      digitalWrite(led3,LOW);
  }
  
  if (distance < 150) {
      digitalWrite(led2, HIGH);
      digitalWrite(led1, LOW);
      digitalWrite(led3,LOW);      
  } 
  
  if (distance < 200) {
    digitalWrite(led3, HIGH);
    digitalWrite(led2, HIGH);
    digitalWrite(led1, LOW);
}
 
  delay(500);
}