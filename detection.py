from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import functions as f 
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode



def chestHunt(window):
    rootX = window.left
    rootY = window.top
    tmp = False
    if pyautogui.locateOnScreen("assets/shield.png",region=(rootX + 620, rootY+660,60,60),grayscale=True) != None:
        tmp = True
    return tmp

def box(window):
    rootX = window.left
    rootY = window.top
    tmp = False
    if pyautogui.locateOnScreen("assets/box.png",region=(rootX + 90, rootY+47,200,500),grayscale=True, confidence=0.8 ) != None:
        tmp = True
    return tmp

def bonusR(window):
    rootX = window.left
    rootY = window.top
    tmp = False
    if pyautogui.locateOnScreen("assets/bonusBarRight.png",region=(rootX + 440, rootY+534,420,60),grayscale=True, confidence=0.8 ) != None:
        tmp = True
    return tmp

def bonusL(window):
    rootX = window.left
    rootY = window.top
    tmp = False
    if pyautogui.locateOnScreen("assets/bonusBarLeft.png",region=(rootX + 440, rootY+534,420,60),grayscale=True, confidence=0.8 ) != None:
        tmp = True
    return tmp


def savior(window):
    rootX = window.left
    rootY = window.top
    
    while(not(pyautogui.locateOnScreen("assets/savior.png",region=(rootX + 150, rootY+250,1000,300)))):
        time.sleep(0.5)
    savior=locateCenterOnScreen("assets/savior.png",region=(rootX + 150, rootY+250,1000,300))
    print(savior)
    return savior.x,savior.y

def bonusClose(window):
    rootX = window.left
    rootY = window.top
    tmp = False
    if pyautogui.locateOnScreen("assets/bonusClose.png",region=(rootX + 660, rootY+550,150,68),grayscale=True, confidence=0.8 ) != None:
        tmp = True
    return tmp