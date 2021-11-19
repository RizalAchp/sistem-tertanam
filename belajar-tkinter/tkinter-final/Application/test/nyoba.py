#!/usr/bin/env python3
from pyfirmata.util import Iterator
from pyfirmata import Arduino
import time
import datetime

board = Arduino('/dev/ttyACM0')
it = Iterator(board)
it.start()

start = 0
end = 0
echopin = board.get_pin('d:12:i')
trigpin = board.get_pin('d:11:o')

trigpin.write(0)
while True:
    try:
        reading = board.digital[11].read()
        # print(reading)
        trigpin.write(1)
        time.sleep(0.00001)
        trigpin.write(0)
        while reading == 0:
            pass
            start = datetime.datetime.now().microsecond
            # print(start)
        while reading is not None:
            pass
            end = datetime.datetime.now().microsecond
            # print(end)
    except KeyboardInterrupt:
        break

    print(float((end-start)*0.034/2))
    time.sleep(1.0)
