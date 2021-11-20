from pymata4.pymata4 import Pymata4
from datetime import datetime
from time import sleep

board = Pymata4('/dev/ttyACM0')
delay = sleep
led_string = [6, 7, 8, 9, ]
buzzer_pin = 5
lm35_pin = 1
trigpin = 11
echopin = 12

for x in led_string:
    board.set_pin_mode_digital_output(x)

board.set_pin_mode_tone(buzzer_pin)
board.set_pin_mode_analog_input(lm35_pin)
board.set_pin_mode_sonar(trigger_pin=trigpin,
                         echo_pin=echopin)
