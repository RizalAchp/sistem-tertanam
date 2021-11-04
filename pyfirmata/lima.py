#!/bin/python
import pyfirmata
import time
from pyfirmata.util import Iterator

board=pyfirmata.Arduino('/dev/tty/ACM0')
it = Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')

while True :
	nilai_analog = analog_input.read()
	print(nilai_analog)
	time.sleep (0.2)
