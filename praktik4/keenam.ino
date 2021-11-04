#include <LiquidCrystal.h>
#define btn1 A0
#define btn2 A1
#define btn3 A2
String a = "KEDIP";
String b = "HIDUP";
String c = "MATI";
String data ;
// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
void setup() {
 Serial.begin(9600);
 // set up the LCD's number of columns and rows:
// lcd.begin(16, 2);
 // Print a message to the LCD.
//lcd.print("Adi Sucipto");
pinMode(btn1, INPUT_PULLUP);
pinMode(btn2, INPUT_PULLUP);
pinMode(btn3, INPUT_PULLUP);
//lcd.init(16,2);
}
void loop() {
 // set the cursor to column 0, line 1
 // (note: line 1 is the second row, since counting begins with 0):

 lcd.setCursor(0,0);
 lcd.print("KIRIM");
 lcd.setCursor(0,1);
if (Serial.available()){
 data = Serial.read();
 Serial.print(data);
 lcd.print(data);

 }

 int n1= digitalRead(btn1);
 int n2= digitalRead(btn2);
 int n3= digitalRead(btn3);

 if (n1==0) {
 lcd.clear();
 Serial.print (a);
 lcd.setCursor(0,1) ;
 lcd.print(a);
 delay(500);
 lcd.clear();
 }
 if (n2==0) {
 lcd.clear();
 Serial.print (b);
 lcd.setCursor(0,1) ;
 lcd.print(b);
 delay(500);
 lcd.clear();

 }
 if (n3==0) {
 lcd.clear();
 Serial.print (c);
 lcd.setCursor(0,1) ;
 lcd.print(c);
 delay(500);
 lcd.clear();
 }
 lcd.setCursor(0, 1);
 // print the number of seconds since reset:
 //lcd.print(m
