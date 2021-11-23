#include <LiquidCrystal.h>
#define btn1 A0
String a = "KEDIP";
String data;

const int rs = 12, end = 11, d4 = 5, d5= 4, d6 = 3, d7 =  2;
LiquidCristal lcd (rs, en, d4, d5, d6, d7);
void setup()
{
    Serial.begin(9600);
    pinMode(btn1, INPUT_PULLUP);
}

void loop()
{
    lcd.setCursor(0,0);
    lcd.print("KIRIM");
    lcd.setCursor(0,1);
    if (Serial.available()){
        data = Serial.read();
        Serial.print(data);
        lcd.print(data);
        }
    int n1= digitalRead(btn1);
    if (n1 == 0){
        lcd.clear();
        Serial.print(a);
        lcd.setCursor(0,1);
        lcd.print(a);
        delay(500);
        lcd.clear();
    }
    lcd.setCursor(0,1);
}
