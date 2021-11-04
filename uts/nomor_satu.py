#!/bin/env python
/* 
 * Disini Saya Menggunakan linux, dimana board mengarahkan
 * pada port /dev/ttyACM0
 */

import pyfirmata

ledPin1 = 9
ledPin2 = 8
ledPin3 = 7
ledPin4 = 6
ledPin = [ledPin1, ledPin2, ledPin3, ledPin4]
board=pyfirmata.Arduino('/dev/ttyACM0')

while True:
	for x in ledPin:
		board.digital[x].write(1)
		print('Led pada Pin', x , "hidup")
		board.pass_time(0.1)
		board.digital[x].write(0)
		print('Led pada Pin', x , "mati")
		board.pass_time(0.1)

