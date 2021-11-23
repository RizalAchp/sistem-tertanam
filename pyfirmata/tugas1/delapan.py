#!/bin/python
import time, datetime

while True:
	waktu = datetime.datetime.now()
	print('%d:%d:%d' % (waktu.hour, waktu.minute , waktu.second))
	time.sleep(1)
