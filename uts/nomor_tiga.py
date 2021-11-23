#!/usr/bin/env python3
/* 
 * Disini Saya Menggunakan linux, dimana board mengarahkan
 * pada port /dev/ttyACM0
 */
import pyfirmata
import time, datetime
from pyfirmata.util import Iterator

board=pyfirmata.Arduino('/dev/ttyACM0')
it = Iterator(board)
it.start ()

analog_in = board.get_pin ('a:1:i')
while True :
	nilai=analog_in.read()
	if nilai is not None:
		waktu = datetime.datetime.now()
		time.sleep(4)
		suhu=5.0*100*nilai
		format_waktu = waktu.hour , waktu.minute , waktu.second
		print('suhu ruangan pada ' '%d:%d:%d' % (format_waktu)\
				,'adalah ', suhu,'celcius')
		time.sleep(0.5)

