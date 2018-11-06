# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)
# Recursive function to toggle pin stat

pwm = Adafruit_PCA9685.PCA9685(0x41)

def motorOn(motor1, motor2, motor3, motor4):
    pwm.set_pwm(motor1, 4096, 0)
    pwm.set_pwm(motor2, 4096, 0)
    pwm.set_pwm(motor3, 4096,0)
    pwm.set_pwm(motor4, 4096,0)
    return

def motorOff(motor1, motor2, motor3, motor4):
    pwm.set_pwm(motor1, 0, 0)
    pwm.set_pwm(motor2, 0, 0)
    pwm.set_pwm(motor3, 0, 0)
    pwm.set_pwm(motor4, 0, 0)
    return

def forwardSpeed(speed, motor1, motor2, motor3, motor4):
    pwm.set_pwm(motor1, speed, 0)
    pwm.set_pwm(motor2, speed, 0)
    pwm.set_pwm(motor3, speed, 0)
    pwm.set_pwm(motor4, speed, 0)
    return
    
def backwardSpeed(speed, motor1, motor2, motor3, motor4):
    pwm.set_pwm(motor1, 0, speed)
    pwm.set_pwm(motor2, 0, speed)
    pwm.set_pwm(motor3, 0, speed)
    pwm.set_pwm(motor4, 0, speed)
    return 

def leftSpeed(speed, motor1, motor2, motor3, motor4):
    forSpeed = 4095 - speed
    pwm.set_pwm(motor1, 0, speed)
    pwm.set_pwm(motor2, forSpeed, 0)
    pwm.set_pwm(motor3, 0, speed)
    pwm.set_pwm(motor4, forSpeed, 0)
    
def rightSpeed(speed, motor1, motor2, motor3, motor4):
    forSpeed = 4095 - speed
    pwm.set_pwm(motor1, forSpeed, 0)
    pwm.set_pwm(motor2, 0, speed)
    pwm.set_pwm(motor3, forSpeed, 0)
    pwm.set_pwm(motor4, 0, speed)


#Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)
	
