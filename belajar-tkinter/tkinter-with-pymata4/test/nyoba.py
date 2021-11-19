from pymata4 import pymata4
import time

trig_pin = 12
echo_pin = 11

board = pymata4.Pymata4('/dev/ttyACM0')


def call_back(data):
    print('jarak: ', data[2])


board.set_pin_mode_sonar(trig_pin, echo_pin, call_back)

while True:
    try:
        time.sleep(1)
        board.sonar_read(trig_pin)
    except Exception:
        board.shutdown()
