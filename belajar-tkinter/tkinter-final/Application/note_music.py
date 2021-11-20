'''
info :
    oke :v, ini saya hanya gabut, banyak string, variable maupun
    maupun array, hanya untuk membuat lagu pada `buzzer`
    disini terdapat2 lagu, yaitu rickroll(LUL), dan canon(classical)
'''

NOTE_B0 = 31    ;NOTE_C1 = 33       ;NOTE_CS1= 35    ;NOTE_D1 = 37
NOTE_DS1= 39    ;NOTE_E1 = 41       ;NOTE_F1 = 44    ;NOTE_FS1= 46
NOTE_G1 = 49    ;NOTE_GS1= 52       ;NOTE_A1 = 55    ;NOTE_AS1= 58
NOTE_B1 = 62    ;NOTE_C2 = 65       ;NOTE_CS2= 69    ;NOTE_D2 = 73
NOTE_DS2= 78    ;NOTE_E2 = 82       ;NOTE_F2 = 87    ;NOTE_FS2= 93
NOTE_G2 = 98    ;NOTE_GS2= 104      ;NOTE_A2 = 110   ;NOTE_AS2= 117
NOTE_B2 = 123   ;NOTE_C3 = 131      ;NOTE_CS3= 139   ;NOTE_D3 = 147
NOTE_DS3= 156   ;NOTE_E3 = 165      ;NOTE_F3 = 175   ;NOTE_FS3= 185
NOTE_G3 = 196   ;NOTE_GS3= 208      ;NOTE_A3 = 220   ;NOTE_AS3= 233
NOTE_B3 = 247   ;NOTE_C4 = 262      ;NOTE_CS4= 277   ;NOTE_D4 = 294
NOTE_DS4= 311   ;NOTE_E4 = 330      ;NOTE_F4 = 349   ;NOTE_FS4= 370
NOTE_G4 = 392   ;NOTE_GS4= 415      ;NOTE_A4 = 440   ;NOTE_AS4= 466
NOTE_B4 = 494   ;NOTE_C5 = 523      ;NOTE_CS5= 554   ;NOTE_D5 = 587
NOTE_DS5= 622   ;NOTE_E5 = 659      ;NOTE_F5 = 698   ;NOTE_FS5= 740
NOTE_G5 = 784   ;NOTE_GS5= 831      ;NOTE_A5 = 880   ;NOTE_AS5= 932
NOTE_B5 = 988   ;NOTE_C6 = 1047     ;NOTE_CS6= 1109  ;NOTE_D6 = 1175
NOTE_DS6= 1245  ;NOTE_E6 = 1319     ;NOTE_F6 = 1397  ;NOTE_FS6= 1480
NOTE_G6 = 1568  ;NOTE_GS6= 1661     ;NOTE_A6 = 1760  ;NOTE_AS6= 1865
NOTE_B6 = 1976  ;NOTE_C7 = 2093     ;NOTE_CS7= 2217  ;NOTE_D7 = 2349
NOTE_DS7= 2489  ;NOTE_E7 = 2637     ;NOTE_F7 = 2794  ;NOTE_FS7= 2960
NOTE_G7 = 3136  ;NOTE_GS7= 3322     ;NOTE_A7 = 3520  ;NOTE_AS7= 3729
NOTE_B7 = 3951  ;NOTE_C8 = 4186     ;NOTE_CS8= 4435  ;NOTE_D8 = 4699
NOTE_DS8= 4978  ;REST    =  0

canon = [
    NOTE_FS4,2, NOTE_E4,2, NOTE_D4,2, NOTE_CS4,2, NOTE_B3,2,
    NOTE_A3,2, NOTE_B3,2, NOTE_CS4,2, NOTE_FS4,2, NOTE_E4,2,
    NOTE_D4,2, NOTE_CS4,2, NOTE_B3,2, NOTE_A3,2, NOTE_B3,2,
    NOTE_CS4,2, NOTE_D4,2, NOTE_CS4,2, NOTE_B3,2, NOTE_A3,2,
    NOTE_G3,2, NOTE_FS3,2, NOTE_G3,2, NOTE_A3,2, NOTE_D4,4,
    NOTE_FS4,8, NOTE_G4,8, NOTE_A4,4, NOTE_FS4,8, NOTE_G4,8,
    NOTE_A4,4, NOTE_B3,8, NOTE_CS4,8, NOTE_D4,8, NOTE_E4,8,
    NOTE_FS4,8, NOTE_G4,8, NOTE_FS4,4, NOTE_D4,8, NOTE_E4,8,
    NOTE_FS4,4, NOTE_FS3,8, NOTE_G3,8, NOTE_A3,8, NOTE_G3,8,
    NOTE_FS3,8, NOTE_G3,8, NOTE_A3,2, NOTE_G3,4, NOTE_B3,8,
    NOTE_A3,8, NOTE_G3,4, NOTE_FS3,8, NOTE_E3,8, NOTE_FS3,4,
    NOTE_D3,8, NOTE_E3,8, NOTE_FS3,8, NOTE_G3,8, NOTE_A3,8,
    NOTE_B3,8, NOTE_G3,4, NOTE_B3,8, NOTE_A3,8, NOTE_B3,4,
    NOTE_CS4,8, NOTE_D4,8, NOTE_A3,8, NOTE_B3,8, NOTE_CS4,8,
    NOTE_D4,8, NOTE_E4,8, NOTE_FS4,8, NOTE_G4,8, NOTE_A4,2,
    NOTE_A4,4, NOTE_FS4,8, NOTE_G4,8, NOTE_A4,4, NOTE_FS4,8,
    NOTE_G4,8, NOTE_A4,8, NOTE_A3,8, NOTE_B3,8, NOTE_CS4,8,
    NOTE_D4,8, NOTE_E4,8, NOTE_FS4,8, NOTE_G4,8, NOTE_FS4,4,
    NOTE_D4,8, NOTE_E4,8, NOTE_FS4,8, NOTE_CS4,8, NOTE_A3,8,
    NOTE_A3,8, NOTE_CS4,4, NOTE_B3,4, NOTE_D4,8, NOTE_CS4,8,
    NOTE_B3,4,NOTE_A3,8, NOTE_G3,8, NOTE_A3,4, NOTE_D3,8,
    NOTE_E3,8, NOTE_FS3,8, NOTE_G3,8,NOTE_A3,8, NOTE_B3,4,
    NOTE_G3,4, NOTE_B3,8, NOTE_A3,8, NOTE_B3,4, NOTE_CS4,8,
    NOTE_D4,8, NOTE_A3,8, NOTE_B3,8, NOTE_CS4,8, NOTE_D4,8,
    NOTE_E4,8, NOTE_FS4,8, NOTE_G4,8, NOTE_A4,2
         ]

rickroll = [
    NOTE_D5,4, NOTE_E5,4, NOTE_A4,4, NOTE_E5,4, NOTE_FS5,4,
    NOTE_A5,16, NOTE_G5,16, NOTE_FS5,8, NOTE_D5,4, NOTE_E5,4,
    NOTE_A4,2, NOTE_A4,16, NOTE_A4,16, NOTE_B4,16, NOTE_D5,8,
    NOTE_D5,16, NOTE_D5,4, NOTE_E5,4, NOTE_A4,4, NOTE_E5,4,
    NOTE_FS5,4, NOTE_A5,16, NOTE_G5,16, NOTE_FS5,8, NOTE_D5,4,
    NOTE_E5,4, NOTE_A4,2, NOTE_A4,16, NOTE_A4,16, NOTE_B4,16,
    NOTE_D5,8, NOTE_D5,16, REST,4, NOTE_B4,8, NOTE_CS5,8,
    NOTE_D5,8, NOTE_D5,8, NOTE_E5,8, NOTE_CS5,8, NOTE_B4,16,
    NOTE_A4,2, REST,4, REST,8, NOTE_B4,8, NOTE_B4,8,
    NOTE_CS5,8, NOTE_D5,8, NOTE_B4,4, NOTE_A4,8, NOTE_A5,8,
    REST,8, NOTE_A5,8, NOTE_E5,4, REST,4, NOTE_B4,8,
    NOTE_B4,8, NOTE_CS5,8, NOTE_D5,8, NOTE_B4,8, NOTE_D5,8,
    NOTE_E5,8, REST,8, REST,8, NOTE_CS5,8, NOTE_B4,8,
    NOTE_A4,4, REST,4, REST,8, NOTE_B4,8, NOTE_B4,8,
    NOTE_CS5,8, NOTE_D5,8, NOTE_B4,8, NOTE_A4,4, NOTE_E5,8,
    NOTE_E5,8, NOTE_E5,8, NOTE_FS5,8, NOTE_E5,4, REST,4,
    NOTE_D5,2, NOTE_E5,8, NOTE_FS5,8, NOTE_D5,8, NOTE_E5,8,
    NOTE_E5,8, NOTE_E5,8, NOTE_FS5,8, NOTE_E5,4, NOTE_A4,4,
    REST,2, NOTE_B4,8, NOTE_CS5,8, NOTE_D5,8, NOTE_B4,8,
    REST,8, NOTE_E5,8, NOTE_FS5,8, NOTE_E5,4, NOTE_A4,16,
    NOTE_B4,16, NOTE_D5,16, NOTE_B4,16, NOTE_FS5,8, NOTE_FS5,8,
    NOTE_E5,4, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,
    NOTE_E5,8, NOTE_E5,8, NOTE_D5,8, NOTE_CS5,16, NOTE_B4,8,
    NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16, NOTE_D5,4,
    NOTE_E5,8, NOTE_CS5,8, NOTE_B4,16, NOTE_A4,8, NOTE_A4,8,
    NOTE_A4,8, NOTE_E5,4, NOTE_D5,2, NOTE_A4,16, NOTE_B4,16,
    NOTE_D5,16, NOTE_B4,16, NOTE_FS5,8, NOTE_FS5,8, NOTE_E5,4,
    NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16, NOTE_A5,4,
    NOTE_CS5,8, NOTE_D5,8, NOTE_CS5,16, NOTE_B4,8, NOTE_A4,16,
    NOTE_B4,16, NOTE_D5,16, NOTE_B4,16, NOTE_D5,4, NOTE_E5,8,
    NOTE_CS5,8, NOTE_B4,16, NOTE_A4,4, NOTE_A4,8, NOTE_E5,4,
    NOTE_D5,2, REST,4, REST,8, NOTE_B4,8, NOTE_D5,8,
    NOTE_B4,8, NOTE_D5,8, NOTE_E5,4, REST,8, REST,8,
    NOTE_CS5,8, NOTE_B4,8, NOTE_A4,4, REST,4, REST,8,
    NOTE_B4,8, NOTE_B4,8, NOTE_CS5,8, NOTE_D5,8, NOTE_B4,8,
    NOTE_A4,4, REST,8, NOTE_A5,8, NOTE_A5,8, NOTE_E5,8,
    NOTE_FS5,8, NOTE_E5,8, NOTE_D5,8, REST,8, NOTE_A4,8,
    NOTE_B4,8, NOTE_CS5,8, NOTE_D5,8, NOTE_B4,8, REST,8,
    NOTE_CS5,8, NOTE_B4,8, NOTE_A4,4, REST,4, NOTE_B4,8,
    NOTE_B4,8, NOTE_CS5,8, NOTE_D5,8, NOTE_B4,8, NOTE_A4,4,
    REST,8, REST,8, NOTE_E5,8, NOTE_E5,8, NOTE_FS5,4,
    NOTE_E5,4, NOTE_D5,2, NOTE_D5,8, NOTE_E5,8, NOTE_FS5,8,
    NOTE_E5,4, NOTE_E5,8, NOTE_E5,8, NOTE_FS5,8, NOTE_E5,8,
    NOTE_A4,8, NOTE_A4,4, REST,4, NOTE_A4,8, NOTE_B4,8,
    NOTE_CS5,8, NOTE_D5,8, NOTE_B4,8, REST,8, NOTE_E5,8,
    NOTE_FS5,8, NOTE_E5,4, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16,
    NOTE_B4,16, NOTE_FS5,8, NOTE_FS5,8, NOTE_E5,4, NOTE_A4,16,
    NOTE_B4,16, NOTE_D5,16, NOTE_B4,16, NOTE_E5,8, NOTE_E5,8,
    NOTE_D5,8, NOTE_CS5,16, NOTE_B4,8, NOTE_A4,16, NOTE_B4,16,
    NOTE_D5,16, NOTE_B4,16, NOTE_D5,4, NOTE_E5,8, NOTE_CS5,8,
    NOTE_B4,16, NOTE_A4,4, NOTE_A4,8, NOTE_E5,4, NOTE_D5,2,
    NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16, NOTE_FS5,8,
    NOTE_FS5,8, NOTE_E5,4, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16,
    NOTE_B4,16, NOTE_A5,4, NOTE_CS5,8, NOTE_D5,8, NOTE_CS5,16,
    NOTE_B4,8, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,
    NOTE_D5,4, NOTE_E5,8, NOTE_CS5,8, NOTE_B4,16, NOTE_A4,4,
    NOTE_A4,8, NOTE_E5,4, NOTE_D5,2, NOTE_A4,16, NOTE_B4,16,
    NOTE_D5,16, NOTE_B4,16, NOTE_FS5,8, NOTE_FS5,8, NOTE_E5,4,
    NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16, NOTE_A5,4,
    NOTE_CS5,8, NOTE_D5,8, NOTE_CS5,16, NOTE_B4,8, NOTE_A4,16,
    NOTE_B4,16, NOTE_D5,16, NOTE_B4,16, NOTE_D5,4, NOTE_E5,8,
    NOTE_CS5,8, NOTE_B4,16, NOTE_A4,4, NOTE_A4,8, NOTE_E5,4,
    NOTE_D5,2, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,
    NOTE_FS5,8, NOTE_FS5,8, NOTE_E5,4, NOTE_A4,16, NOTE_B4,16,
    NOTE_D5,16, NOTE_B4,16, NOTE_A5,4, NOTE_CS5,8, NOTE_D5,8,
    NOTE_CS5,16, NOTE_B4,8, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16,
    NOTE_B4,16, NOTE_D5,4, NOTE_E5,8, NOTE_CS5,8, NOTE_B4,16,
    NOTE_A4,4, NOTE_A4,8, NOTE_E5,4, NOTE_D5,2, REST,4
            ]

'''
    dari array diatas dapat di lihat bahwa terdapat 2 value,
    yaitu value frequensi dan value waktu/delay dari frequensi
    pada variable `NOTE`.
    oleh karena itu saya buat `_for` function dibawah untuk mengambil
    value dari array dan di bagi menjadi 2 variable
    yaitu
    -> `note_len`   sebagai delay frequensi
    -> `note_freq`  sebagai nilai frequensi
'''
note_len= []
note_freq = []

## RICK ROLLS
for i in range(0, len(rickroll)):
    if i % 2:
        # value waktu saya bagi2 untuk menkonversikan
        # kedalam satuan miliseconds
        note_len.append(float((60.0*4/200)/rickroll[i]))
    else :
        # value saya bagi 0.05 karena buzzer pada pyfirmata
        # tidak dapat menggunakan value freq
        note_freq.append(float(0.05*rickroll[i]))

## CANON IN D CLASSIC
# for i in range(0, len(canon)):
#     if i % 2:
#         note_len.append(float((6*4/100/canon[i])))
#     else :
#         note_freq.append(float(0.001*canon[i]))
# print(canon)
# print(note_len)
# print(note_freq)

'''TESTING WITH PYFIRMATA ( gabisa pake frequensi tone, sucks )'''
# from pyfirmata.util import Iterator
# import  pyfirmata
# board = pyfirmata.Arduino('/dev/ttyACM0')
# buzzer_pin = board.get_pin('d:5:p')
# it = Iterator(board)
# it.start()

# for x,(durasi, freq) in enumerate(zip(note_len, note_freq)):
#     buzzer_pin.write(freq)
#     board.pass_time(durasi)
#     buzzer_pin.write(0)
#     board.pass_time(durasi)

'''TESTING PADA PYMATA ( sejauh ini hasilnya sangat meemuaskan )'''
# from pymata4 import pymata4
# board = pymata4.Pymata4

# buzzer_pin = 5
# board.set_pin_mode_tone(buzzer_pin)
# while True:
#     for x,(durasi, freq) in enumerate(zip(note_len, note_freq)):
#         board.play_tone(buzzer_pin, freq,durasi)
#         waktu=float(durasi/1000*0.9)
#         time.sleep(waktu)
#         board.play_tone_off(buzzer_pin)
#         print(x,durasi,waktu)
