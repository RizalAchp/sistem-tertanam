int pinLed[] = {5, 6, 9, 10};
int timer = 500;
int btn3 = 4;
int pinBuzz = 11;
int jmlPin = 4;

void setup() 
{
    for (int i = 0; i < jmlPin; i++) 
    {
        pinMode(pinLed[i], OUTPUT);
    }

    pinMode(5, OUTPUT);
    pinMode(6, OUTPUT);
    pinMode(9, OUTPUT);
    pinMode(10, OUTPUT);
    pinMode(btn3, INPUT);
    pinMode(pinBuzz, OUTPUT);
    Serial.begin(9600);
}

void loop() 
{
    if (digitalRead(btn3) == 1) 
    {
        Serial.println("input 1 --> 4 Led berkedip\ninput 2 --> Sirine Bazzer\ninput 3 --> Led dan buzzer berurutan\ninput 4 --> 4 Led PWM");
        delay(1000);
    }

    if (Serial.available()) 
    {
        int kondisi = Serial.parseInt();
        int i = 0;
        
        while (kondisi == 1)
        {
            digitalWrite(5, HIGH);
            digitalWrite(6, HIGH);
            digitalWrite(9, HIGH);
            digitalWrite(10, HIGH);
            delay(timer);
            digitalWrite(5, LOW);
            digitalWrite(6, LOW);
            digitalWrite(9, LOW);
            digitalWrite(10, LOW);
            delay(timer);
            Serial.println("4 LED BERKEDIP");
            if (i > 3)
                break;
            i++;
        }

        while (kondisi == 2) 
        { 
            // masih ada bug, loop tidak dapat di berhentikan 
            Serial.println("Sirine Buzzer");
            for (i = 300; i < 800; i++) {
                tone(pinBuzz, i);
                delay(5);
            }
            for (i = 800; i > 300; i--) {
                tone(pinBuzz, i);
                delay(5);
            }
             /* 
              *  if (i > 3)
              *    break;
              * i++; 
              */
        }
        
        while (kondisi == 3)
        {
            Serial.println("LED dan Buzzer berurutan");
            for (int i = 0; i < jmlPin; i++) {
                digitalWrite(pinLed[i], HIGH);
                tone(pinBuzz, 500);
                delay(timer);
                digitalWrite(pinLed[i], LOW);
                noTone(pinBuzz);
                delay(timer);
            }
            if (i > 3)
                break;
            i++;
        }
        
        while (kondisi == 4)
        {
            Serial.println("4 LED PWM");
            for (int ledVal = 255; ledVal >= 0; ledVal -= 1) {
                analogWrite(5, ledVal);
                analogWrite(6, ledVal);
                analogWrite(9, ledVal);
                analogWrite(10, ledVal);
                delay(15);
            }
            if (i > 3)
                break;
            i++;
        }
    }
}
