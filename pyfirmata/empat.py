#!/bin/python
import pyfirmata
import time
from pyfirmata.util import Iterator

button1=3
pinled1=9
board=pyfirmata.Arduino('/dev/ttyACM0')
it = Iterator(board)

it.start ()
board.digital[button1].mode = pyfirmata.INPUT
btn1 = board.digital[button1].read()

if btn1 == 1 :
	board.digital[pinled1].write(0)
else :
	board.digital[pinled1].write(1)
	time.sleep(1)
