#!/usr/bin/env python3
/* 
 * Disini Saya Menggunakan linux, dimana board mengarahkan
 * pada port /dev/ttyACM0
 */
import time
import board
import adafruit_hcsr04 // library adafruit
import pyfirmata

led1 = 6
led2 = 7
led3 = 8
led4 = 9

board = pyfirmata.Arduino('/dev/ttyACM0')
trigPin = board.D1
echoPin = board.D2
sonar = adafruit_hcsr04.HCSR04(trigPin, echoPin)
jarak = sonar.distance
while True:
    try:
    print(jarak)i
    if jarak =< 50:
        print('jarak diatas 50 cm!')
        board.digital(led1).write(1)
        board.digital(led2).write(0)
        board.digital(led3).write(0)
        board.digital(led4).write(0)
        board.pass_time(0.1)

    if jarak < 100:
        print('jarak diatas 100 cm!')
        board.digital(led1).write(1)
        board.digital(led2).write(1)
        board.pass_time(0.1)

    if jarak < 150:
        print('jarak diatas 150 cm!')
        board.digital(led1).write(1)
        board.digital(led2).write(1)
        board.digital(led3).write(1)
        board.pass_time(0.1)

    if jarak < 200:
        print('jarak diatas 200 cm!')
        board.digital(led1).write(1)
        board.digital(led2).write(1)
        board.digital(led3).write(1)
        board.digital(led4).write(1)
        board.pass_time(0.1)
except RuntimeError:
    print('Error! tidak dapat membaca sensor!')
time.sleep(0.1)

    
