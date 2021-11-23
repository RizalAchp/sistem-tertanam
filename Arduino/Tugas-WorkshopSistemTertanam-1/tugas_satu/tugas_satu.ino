int i; 
int timer = 500;
int pinLed[] = {10, 9, 6, 5};
int pinBuzz = 11; 
int jmlPin = 4;
int btn1 = 2;
int bacaBtn, lastBtn, cond = 0;

void setup()
{
  for (int i = 0; i < jmlPin; i++)
  {
    pinMode(pinLed[i], OUTPUT);
  }
  pinMode(btn1, INPUT);
  pinMode(pinBuzz, OUTPUT);
}

void loop()
{ 
   /* ini fungsi LED yang berjalan dari pin 10 dan ke 5
    * dan untuk menjalankan loop, tekan push button 1 dahulu.
    */
  bacaBtn = digitalRead (btn1);
  if ((bacaBtn == HIGH) && (lastBtn == LOW))
  {
    cond = 1 - cond;
    delay(10);
  }
  lastBtn = bacaBtn;
  if (cond == 1)
  {
    for (int i = 0; i < jmlPin; i++) {
      digitalWrite(pinLed[i], HIGH);
      delay(timer);
      digitalWrite(pinLed[i], LOW);
      delay(timer);
    }
    tone(pinBuzz, 600);
    delay(timer);
    noTone(pinBuzz);
    delay(timer);
  }
  else {// menstop loop dengan menekan tombol 1 selama kurang lebih dari 3 detik
    for (int i = 0; i < jmlPin; i++)
    {
      digitalWrite(pinLed[i], LOW);
    } 
    noTone(pinBuzz);
  }
}
