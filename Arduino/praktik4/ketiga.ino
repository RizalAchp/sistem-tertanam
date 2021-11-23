#include <LiquidCrystal.h>
#define btn3 A2
String c = "MATI";
String data ;
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
void setup() {
 Serial.begin(9600);
pinMode(btn3, INPUT_PULLUP);
}
void loop() {
 lcd.setCursor(0,0);
 lcd.print("KIRIM");
 lcd.setCursor(0,1);
if (Serial.available()){
 data = Serial.read();
 Serial.print(data);
 lcd.print(data);
 }
 int n3= digitalRead(btn3);
 if (n3==0) {
 lcd.clear();
 Serial.print (c);
 lcd.setCursor(0,1) ;
 lcd.print(c);
 delay(500);
 lcd.clear();
 }
 lcd.setCursor(0, 1);
 }
