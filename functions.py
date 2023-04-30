from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

chestBrown = (174, 108, 55)
saviorYellow = (255, 235, 4)
def chestHunt(saviorX,saviorY,window):
    firstChestX = window.left + 220
    firstChestY = window.top + 500
    if((saviorX > firstChestX -20 and saviorX < firstChestX+20)and((saviorY > firstChestY -20 and saviorY < firstChestY+20))):
        win32api.SetCursorPos((firstChestX+95,firstChestY))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(2)
        h = 0
        v = 0
        x = firstChestX
        y = firstChestY
        while(v<3):  
            while(h<10):
                win32api.SetCursorPos((x,y))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                time.sleep(2)
                if pyautogui.locateCenterOnScreen("assets/close.png",grayscale=True) != None:
                    v=4
                    h=11
                x+=95
                h+=1
            y-=95
            x-=95*10    
            v+=1
            h=0
    else:
        win32api.SetCursorPos((firstChestX,firstChestY))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(2)
        win32api.SetCursorPos((saviorX,saviorY))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(2)
        h = 0
        v = 0
        x = firstChestX
        y = firstChestY
        while(v<3):  
            while(h<10):
                win32api.SetCursorPos((x,y))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                time.sleep(2)
                x+=95
                h+=1
                if pyautogui.locateOnScreen("assets/close.png",grayscale=True,confidence= 0.8)!= None:
                    v=4
                    h=11
            y-=95
            x-=95*10    
            v+=1
            h=0
    time.sleep(10)
    close= pyautogui.locateCenterOnScreen("assets/close.png",grayscale=True,confidence= 0.8)
    win32api.SetCursorPos((close.x,close.y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

        


def chestClick():
    x=262
    y=520
    h = 0
    v = 0
    while(v<3):  
        while(h<10):
            win32api.SetCursorPos((x,y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            time.sleep(2)
            x+=95
            h+=1
        y-=95
        x-=95*10    
        v+=1
        h=0  

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def highJump(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def jumpShoot(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    i=0
    while(i<=8):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.05)
        i +=1

def shoot(x,y):
    win32api.SetCursorPos((x,y))
    i=0
    while(i<4):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.2)
        i +=1
def bonus(rootX,rootY):
    tmpX = rootX + 820
    tmpY = rootY + 620
    win32api.SetCursorPos((tmpX,tmpY))
    pyautogui.dragTo(tmpX+340, tmpY, 2, button='left') 

def boost(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

def bonusDrag(window,dir):
    rootX = window.left
    rootY = window.top
    if(dir=="r"):
        tmpX = rootX +820
        tmpY = rootY +550
        win32api.SetCursorPos((tmpX,tmpY))
        pyautogui.dragTo(tmpX-340, tmpY, 2, button='left')
    if(dir=="l"):
        tmpX = rootX + 480
        tmpY = rootY + 550
        win32api.SetCursorPos((tmpX,tmpY))
        pyautogui.dragTo(tmpX+340, tmpY, 2, button='left')