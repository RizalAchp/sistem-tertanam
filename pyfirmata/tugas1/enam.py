#!/bin/python
import pyfirmata
import time

board=pyfirmata.Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start ()

analog_input = board.get_pin ('a:0:i')
pin_led = board.get_pin('d:9:p')
while True :
	nilai_analog = analog_input.read() 
	if nilai_analog is not None :
		pin_led.write(1)
		time.sleep(delay)
		pin_led.write(0)
		time.sleep(delay)
	else :
		time.sleep(0.1)
	print (nilai_analog)
