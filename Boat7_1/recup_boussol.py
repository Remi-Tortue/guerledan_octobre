import imu9_driver_v2 as imudrv

imu = imudrv.Imu9IO()

for i in range (20) :
	magx,magy,magz = imu.read_mag_raw()
	print("mag x,y,z =",magx,magy,magz)
	