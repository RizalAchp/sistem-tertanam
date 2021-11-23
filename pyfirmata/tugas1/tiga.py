#!/bin/python
import pyfirmata
from time import sleep

pin = 5
board=pyfirmata.Arduino('/dev/ttyACM0')

while True:
	board.digital[pin].write(1)
	sleep(1)
	board.digital[pin].write(0)
	sleep(1)
