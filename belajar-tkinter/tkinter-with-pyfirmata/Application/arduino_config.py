import time
import datetime
from pyfirmata import Arduino, util

board = Arduino('/dev/ttyACM0')

it = util.Iterator(board)
it.start()

waktu = time.sleep
ledPin = [6, 7, 8, 9]
analog_suhu = board.get_pin('a:1:i')
buzzer_pin = board.get_pin('d:5:p')
