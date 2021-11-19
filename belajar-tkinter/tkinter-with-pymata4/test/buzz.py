from pymata4 import pymata4
import time
from ..note import *

board = pymata4.Pymata4('/dev/ttyACM0')

buzzer_pin = 5
board.set_pin_mode_tone(buzzer_pin)
while True:
    for x in note_freq:
        for y in note_len:
            board.play_tone(buzzer_pin, x, y)
