#!/usr/bin/python3
import pyfirmata
import time
import datetime
from pyfirmata.util import Iterator

board = pyfirmata.Arduino('/dev/ttyACM0')
it = Iterator(board)
it.start()
tanggal = datetime.datetime.now()
waktu = time.sleep
ledPin = [6, 7, 8, 9]
analog_suhu = board.get_pin('a:1:i')
analog_buzz = board.get_pin('d:5:p')


def led_blink():
    for x in ledPin:
        board.digital[x].write(1)
        print('led', x, 'hidup')
        board.pass_time(0.3)
        board.digital[x].write(0)
        print('led', x, 'mati')
        waktu(0.3)


def buzzer():
    print('wiuwiu')
    analog_buzz.write(0.2)
    board.pass_time(0.5)
    analog_buzz.write(0.6)
    board.pass_time(0.5)
    analog_buzz.write(0.8)
    board.pass_time(0.5)
    analog_buzz.write(0)


def sensor_suhu():
    nilai = analog_suhu.read()
    if nilai is not None:
        waktu(4)
        suhu = 5.0*100*nilai
        format_waktu = tanggal.hour, \
            tanggal.minute, tanggal.second
        print('suhu ruangan pada' '%d:%d:%d' %
              (format_waktu), 'adalah', suhu, 'celcius')
        waktu(0.5)


def sensor_sonic():
    print("bug, puseng cok")
