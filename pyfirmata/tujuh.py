#!/bin/python
import pyfirmata
import time
from pyfirmata.util import Iterator

board=pyfirmata.Arduino('/dev/ttyACM0')
it = Iterator(board)
it.start ()

analog_input = board.get_pin ('a:1:i')
while True :
	nilai_analog=analog_input.read()
	if nilai_analog is not None:
		suhu=5.0*100*nilai_analog
		print(suhu,'celcius')
		time.sleep(0.2)
