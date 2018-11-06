import serial
import RPi.GPIO as GPIO
from time import sleep

ser = serial.Serial(port='/dev/ttyACM0',baudrate = 96000,timeout = 1)
backInfo = 0 

def sensorData(pin):
        global backInfo
	response = ser.readline()
	if len(response[16:-1]) > 0 and len(response[16:-1]) < 15:
            if(pin == 0):
                backInfo = float(response[16:-1])
                return float(response[16:-1])
            elif(pin==1):
                response = ser.readline()
                backInfo = float(response[16:-1])
                return float(response[16:-1])
            else:
                return backInfo
        else:
            return backInfo;

