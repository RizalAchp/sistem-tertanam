#include <LiquidCrystal.h>
#define btn2 A1
String b = "HIDUP";
String data ;
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
void setup() {
 Serial.begin(9600);
pinMode(btn2, INPUT_PULLUP);
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
 int n2= digitalRead(btn2);

 if (n2==0) {
 lcd.clear();
 Serial.print (b);
 lcd.setCursor(0,1) ; 
 lcd.print(b);
 delay(500);
 lcd.clear();
 }
 lcd.setCursor(0, 1);
}
