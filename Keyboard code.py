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
movement3 = 'Stop'
def on_press(key):
    if key == keyboard.KeyCode.from_char('w'):
        movement = 'Go'
    if key == keyboard.KeyCode.from_char('a'):
        if movement == 'Go':
            movement2 = 'Low Power'
            movement3 = 'Go'
        else:
            movement2 = 'Back'
            movement3 = 'Go'
        
    if key == keyboard.KeyCode.from_char('d'):
        movement = 'Go'
        movement2 = 'Back'
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        try:
            if movement == 'Stop' and movement2 == 'Stop' and movement3 == 'Stop':
                print('Stopped')
            if movement == 'Go':
                print('Forward')
            if movement == 'Go' and movement2 == 'Back':
                print('Right')
            if movement2 == 'Back' and movement3 == 'Go':
                print('Left')
            if movement2 == 'Low Power' and movement3 == 'Go':
                
        except UnboundLocalError:
            pass
            
        
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
    


def on_release(key):
    if key == keyboard.KeyCode.from_char('a'):
        print('A STOPPED')
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
        