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

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685(0x41)

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

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
    
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
        forwardSpeed(2000,0,5,6,11)
        motorOff(2,4,7,9)
        motorOn(1,3,8,10)
	
	time.sleep(1)
	
	motorOff(1,3,8,10)
	backwardSpeed(2000,0,5,6,11)
        motorOn(2,4,7,9)
        
	time.sleep(1)
	
	motorOff(1,3,8,10)
	motorOff(2,4,7,9)
        
        time.sleep(1)
	
