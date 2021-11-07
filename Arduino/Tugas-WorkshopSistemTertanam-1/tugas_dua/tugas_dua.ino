int timer = 500;
int btn2 = 3;
int bacaBtn, lastBtn, cond = 0;

void setup()
{
  pinMode(btn2, INPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop()
{
  /*
   * ini untuk led yang berjalan pin 5 ke pin 10 (atau sebaliknya dari yang sebelumnya)
   * sama seperti sebelumnya, untuk menjalankan loop, tekan tombol 2
   */
  bacaBtn = digitalRead (btn2);
  if ((bacaBtn == HIGH) && (lastBtn == LOW))
  {
    cond = 1 - cond;
    delay(10);
  }
  lastBtn = bacaBtn;
  if(cond == 1)
  {
      for (int ledVal = 255; ledVal > 0; ledVal -= 1)
      {
        digitalWrite(5, ledVal);
        delay(timer);
        digitalWrite(6, ledVal);
        delay(timer);
        digitalWrite(9, ledVal);
        delay(timer);
        digitalWrite(10, ledVal);
        delay(timer);
      }
      for (int ledVal =  0; ledVal < 255; ledVal += 1)
      {
        digitalWrite(5, ledVal);
        delay(timer);
        digitalWrite(6, ledVal);
        delay(timer);
        digitalWrite(9, ledVal);
        delay(timer);
        digitalWrite(10, ledVal);
        delay(timer);
      }
  }
  else 
  {
    digitalWrite(5, LOW);
    digitalWrite(6, LOW);
    digitalWrite(9, LOW);
    digitalWrite(10, LOW);
  }
}
