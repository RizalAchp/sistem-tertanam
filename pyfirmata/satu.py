#!/bin/python
import pyfirmata

pin=6
board=pyfirmata.Arduino('/dev/ttyACM0')

while True:
    board.digital[pin].write(1)
    board.pass_time(1)
    board.digital[pin].write(0)
    board.pass_time(1)

