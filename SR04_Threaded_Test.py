#!/usr/bin/python3
# March 2018
# Multithreaded HC-SR04 sonar sensor controller by Raspberry Pi 3 via GPIO

import SR04                                  # RPi HC-SR04 multi-threaded
# import SR04_pigpio as SR04
from time import sleep
from datetime import datetime

#   Initialize multi-threaded HC-SR04 sonic sensor
DistThread = SR04.ChkDist(1,"ChkDist-1")
DistThread.start()

cnt = 0

datetime.now()

#for loop in range(0,cnt):
try:
	while True:
		distance = SR04.getDist()
		print("{4} {3} {0:.2f}cm  {1:.2f}in  {2:.2f}ft".format(distance,(distance * 0.394),((distance * 0.394)/12),datetime.now(),cnt))
		cnt += 1
except KeyboardInterrupt:
	print(" shut'n me-self down.. ")
	sleep(2)
	SR04.stop()
	
# DistThread.stop()


