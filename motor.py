import RPi.GPIO as io
import sys, tty, termios, time
io.setmode(io.BCM)

in1_pin = 4
in2_pin = 17

io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)

def clockwise():
	io.output(in1_pin,True)
	io.output(in2_pin, False)
        return;

def counter_clockwise():
	io.output(in1_pin, False)
	io.output(in2_pin, True)
	return;

def stop():
	io.output(in1_pin, False)
	io.output(in2_pin, False)
	return;

def getch():
        fd = sys.stdin.fileno()
	sys.stdin.flush()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
                
stop()

while True:
	#cmd = raw_input("Enter Value: ")
	#direction = cmd[0]
        direction = getch()
	print(direction)
	if direction == "f":
        	clockwise()
		direction = getch()
        elif direction == "r":
        	counter_clockwise()
		direction = getch()
	else:
		stop()

	if direction  == "a":
        	break
