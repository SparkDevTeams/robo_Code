import time
import RPi.GPIO as GPIO
servo = 18

GPIO.setmode(GPIO.BCM)

GPIO.setup(servo,GPIO.OUT)

p = GPIO.PWM(servo, 50)

p.start(7.5)



try:
        
	#def getch():
        #       fd = sys.stdin.fileno()
        #      old_settings = termios.tcgetattr(fd)
        #        try:
        #           tty.setraw(sys.stdin.fileno())
        #           ch = sys.stdin.read(1)
        #        finally:
        #            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        #            return ch
	while True: 
		#for  duty_cycle in range(3, 15, 1):
		#	p.ChangeDutyCycle(duty_cycle)
		#	time.sleep(0.1)
		#for duty_cycle in range(15, 3, -1):
		#	p.ChangeDutyCycle(duty_cycle)
		#	time.sleep(0.1)
		
		#char = getch()
		
		
		for degreeChange in range (0, 180, 10):
                    duty_cycle = degreeChange/12
                    p.ChangeDutyCycle(duty_cycle)
                    time.sleep(0.2)
                    
                    print(duty_cycle)

except KeyboardInterrupt:
	GPIO.cleanup()
