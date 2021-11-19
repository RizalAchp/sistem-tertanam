from pymata4 import pymata4
import time

board = pymata4.Pymata4('/dev/ttyACM0')
lm35_pin = 1


def callback_lm(data):
    data_suhu = data[2]
    suhu = 5.0*data_suhu/10.23
    print(suhu, ' derajat celcius')


while True:
    board.set_pin_mode_analog_input(lm35_pin, callback_lm)
    try:
        val = board.analog_read(lm35_pin)

    except KeyboardInterrupt:
        board.shutdown()
    time.sleep(4)
