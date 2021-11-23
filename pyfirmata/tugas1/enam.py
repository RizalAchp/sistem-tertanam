#!/bin/python
import time
from pyfirmata import Arduino, util

board = Arduino('/dev/ttyACM0')
it = util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')
pin_led = board.get_pin('d:9:p')
delay = time.sleep
while True:
    nilai_analog = analog_input.read()
    if nilai_analog is not None:
        pin_led.write(1)
        delay(0.1)
        pin_led.write(0)
        delay(0.1)
    else:
        delay(0.1)
    print(nilai_analog)
