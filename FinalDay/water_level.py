import RPi.GPIO as GPIO
from time import sleep
import sensor

def waterData():
	level = sensor.sensorData(1)
	if level<15 and level > -1:
		return 'Robot on Dry Land'

	elif level > 15:
		return 'Robot in Water!'

	else:
		return 'Error With Sensor'


print(waterData())
