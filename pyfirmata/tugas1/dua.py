#!/bin/env python
import pyfirmata
pinA=6
pinB=7
pinC=8
pinD=9
board=pyfirmata.Arduino('/dev/ttyACM0')

while True:
	board.digital[pinA].write(1)
	board.digital[pinB].write(1)
	board.digital[pinC].write(1)
	board.digital[pinD].write(1)
	board.pass_time(1)
	board.digital[pinA].write(0)
	board.digital[pinB].write(0)
	board.digital[pinC].write(0)
	board.digital[pinD].write(0)
	board.pass_time(1)

