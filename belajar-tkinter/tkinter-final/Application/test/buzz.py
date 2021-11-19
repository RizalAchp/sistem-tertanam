import pyfirmata
from pyfirmata.util import Iterator
import math

board = pyfirmata.Arduino("/dev/ttyACM0")

# connect piezo to pin 9 to use PWM
SENSOR_PIN = 0
PIEZO_PIN = board.get_pin('d:5:p')

it = Iterator(board)
it.start()

board.analog[SENSOR_PIN].enable_reporting()

# check buzzer is working
# PIEZO_PIN.write(0.200)
# board.pass_time(0.5)
# PIEZO_PIN.write(0.600)
# board.pass_time(0.5)
# PIEZO_PIN.write(0.800)
# board.pass_time(0.5)
PIEZO_PIN.write(0)

# while True:
#     light_level = board.analog[SENSOR_PIN].read()
#     if (light_level != None):
#         print(light_level)
#         # you may wish to adjust the raw reading here to get a better range of beeps
#         buzzer_value = light_level
#         PIEZO_PIN.write(buzzer_value)
#         board.pass_time(0.5)
#         PIEZO_PIN.write(0)
#         board.pass_time(0.5)
