import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_BUTTON = KeyCode(char="t")
moving = False
clicking = False
mouse = Controller()

def move():
    while True:
        if moving:
            mouse.move(500,0)
            time.sleep(0.1)
            mouse.move(0,200)
            time.sleep(0.1)
            mouse.move(-500,0) 
            time.sleep(0.1)
            mouse.move(0,-200)
        time.sleep(0.1)
 

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 5)
            mouse.click(Button.right, 1)
        time.sleep(0.001)

def toggle_event(key):
    if key == TOGGLE_BUTTON:
        global clicking
        global moving
        clicking = not clicking
        moving = not moving

click_thread = threading.Thread(target=clicker)
move_thread = threading.Thread(target=move)

move_thread.start()
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()