from time import sleep
import RPi.GPIO as GPIO
import l293.driver as l293d
#GPIO.setmode(GPIO.BOARD)

#GPIO.setup(16, GPIO.OUT)
#GPIO.setup(18, GPIO.OUT)

# pin 22 is enable pin
#GPIO.setup(22, GPIO.OUT)

#pwm = GPIO.PWM(22,100)

#pwm.start(0)
motor1 = l293d.motor(22,18,16)

# foward direction
#GPIO.output(16, True)
#GPIO.output(18, False)
for i in range(0,150):
    motor1.clockwise()
    
l293d.cleanup()
# set pwm to 50% and enable pin on
#pwm.ChangeDutyCycle(50)
#GPIO.output(22, True)
#sleep(2)

# code above makes motors go foward for 2 seconds at 50% power

