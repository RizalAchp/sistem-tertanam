from pymata4 import pymata4
import time

var = [6, 7, 8, 9]

board = pymata4.Pymata4('/dev/ttyACM0')
while True:
    for x in var:
        board.set_pin_mode_digital_output(x)
        board.digital_write(x, 1)
        time.sleep(0.5)
        board.digital_write(x, 0)
