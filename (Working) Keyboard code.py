# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 19:31:56 2018

@author: Rez
"""
import sys
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
def on_press(key):
    if key == keyboard.KeyCode.from_char('w'):
        print('Forward')
    if key == keyboard.KeyCode.from_char('a'):
        print('Left')
    if key == keyboard.KeyCode.from_char('d'):
        print('Right')
    if key == keyboard.KeyCode.from_char('s'):
        print('Backward')
    if key == keyboard.KeyCode.from_char('1'):
        print('1')
    if key == keyboard.KeyCode.from_char('2'):
        print('2')
    if key == keyboard.KeyCode.from_char('3'):
        print('3')
    if key == keyboard.KeyCode.from_char('4'):
        print('4')
    if key == keyboard.KeyCode.from_char('5'):
        print('5')
        
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    print('{0} released'.format(
        key))
    try:
        combo.remove(key)
    except KeyError:
        pass
    except AttributeError:
        pass
    

# Collect events until released
#with keyboard.Listener(
#        on_press=on_press,
#        on_release=on_release) as listener:
#    listener.join()
while True:
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()
        