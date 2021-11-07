int i;                              // variable loop
int timer = 500;                    // variable waktu
int pinLed[]={6,7,8,9};             // variable pinLed
int jumlahPin = 4;                  // variable jumlah Pin

void setup() {
  for (int i=0; i<jumlahPin; i++){  // loop setiap jumlah pin
    pinMode(pinLed[i], OUTPUT);     // setup pin LED
  }
}
void loop() {
  for (int i=0; i<jumlahPin; i++){  // func loop
    digitalWrite(pinLed[i],HIGH);   // LED hidup
    delay(timer);                   // delay sesuai variable waktu yang sudah ditentukan
    digitalWrite(pinLed[i],LOW);    // LED hidup  
    delay(timer);                   // delay sesuai variable waktu yang sudah ditentukan
  }
}