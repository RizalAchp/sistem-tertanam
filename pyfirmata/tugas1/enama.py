#!/bin/python
import pyfirmata
import time
from pyfirmata.util import Iterator as Iter

board=pyfirmata.Arduino('/dev/ttyACM0')
it = Iter(board)
it.start ()

analog_input = board.get_pin ('a:0:i')
pin_led = board.get_pin('d:9:p')
while True :
	nilai_analog = analog_input.read() 
	if nilai_analog is not None :
		pin_led.write(nilai_analog)
		print (nilai_analog)
