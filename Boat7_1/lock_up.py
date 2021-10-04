import time
import sys
import imu9_driver_v2 as imudrv
import gps_driver_v2 as gpsdrv
import arduino_driver_v2 as arddrv
import encoders_driver_v2 as encoddrv

imu = imudrv.Imu9IO()
gps = gpsdrv.GpsIO()
ard = arddrv. ArduinoIO()
encod = encoddrv.EncoderIO()

magx,magy,magz = imu.read_mag_raw()
lock_up = zeros(10)

for u2 in range (10) :
	for u1 in range (10) :
		ard.send_arduino_cmd_motor(0,0) 
		imput ("ready ?")
		ard.send_arduino_cmd_motor(u1,u2) #on alume le moteur
		val_case = [0]
		for t in range (50) : #on recuperer des valeurs d'angle pendant 5s
			magx,magy,magz = imu.read_mag_raw()
			theta = cap(magx,magy) # fonction à coder
			val_case.append(sin(theta - val_case[t-1]))
			pause (0.1)
		m = moy (val_case)
		lock_up[u1,u2] = m

bon_u1_u2 = []
for u2 in lock_up :
	n = u2 [0]
	for i in u2 :
		if abs(i) < n:
			n = i
	bon_u1_u2.append (n)
print(bon_u1_u2)
