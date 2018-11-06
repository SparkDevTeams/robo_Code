# -*- coding: utf-8 -*-
#"""
#Created on Wed Oct 17 19:31:56 2018

#@author: Rez
#"""
import sys
import motors
import time
from pynput import keyboard
from pynput.keyboard import Key, Controller
FORWARD = {keyboard.KeyCode.from_char('w')}
LEFT = {keyboard.KeyCode.from_char('a')}
FORWARD_LEFT = {keyboard.KeyCode.from_char('w'), keyboard.KeyCode.from_char('a')}
FORWARD_RIGHT = {keyboard.KeyCode.from_char('w'), keyboard.KeyCode.from_char('d')}
BACKWARD_LEFT = {keyboard.KeyCode.from_char('w'), keyboard.KeyCode.from_char('a')}
BACKWARD_RIGHT = {keyboard.KeyCode.from_char('w'), keyboard.KeyCode.from_char('a')}
combo = set()
keyboard2 = Controller()
listener = keyboard.Listener
test1 = 0
test2 = 0
movement = 'Stop'
movement2 = 'Stop'
currSpeed = 3000

def on_press(key):
	global currSpeed
	if key == keyboard.KeyCode.from_char('1'):
		print('1')
		currSpeed = 2000
	if key == keyboard.KeyCode.from_char('2'):
		print('2')
		currSpeed = 2500
	if key == keyboard.KeyCode.from_char('3'):
		print('3')
		currSpeed = 3000
	if key == keyboard.KeyCode.from_char('4'):
		print('4')
		currSpeed = 3500
	if key == keyboard.KeyCode.from_char('5'):
		print('5')
		currSpeed = 4000
	if key == keyboard.KeyCode.from_char('w'):
		print('Forward')
		motors.forwardSpeed((4095-currSpeed),0,5,6,11)
		motors.motorOff(2,4,7,9)
		motors.motorOn(1,3,8,10)
	if key == keyboard.KeyCode.from_char('a'):
		print('Left')
	if key == keyboard.KeyCode.from_char('d'):
		print('Right')
	if key == keyboard.KeyCode.from_char('s'):
		print('Backward')
		motors.motorOff(1,3,8,10)
		motors.backwardSpeed(currSpeed,0,5,6,11)
		motors.motorOn(2,4,7,9)

def on_release(key):
	if key == keyboard.Key.esc:
        # Stop listener
		return False
	else:
		motors.motorOff(1,3,8,10)
		motors.motorOff(2,4,7,9)

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
while True:
	with keyboard.Listener( on_press=on_press, on_release=on_release) as listener:
		listener.join()
