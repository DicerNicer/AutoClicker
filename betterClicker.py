from pyautogui import *
import pyautogui
import time
import win32api, win32con
import functions as f 
import threading
from pynput.keyboard import Listener, KeyCode
import detection as det
import tkinter as tk

idleWindow = pyautogui.getWindowsWithTitle("Idle Slayer")[0]
rootX = idleWindow.left
rootY = idleWindow.top

clicking = False
TOGGLE_BUTTON = KeyCode(char="t")




def gui():
    # Erstellen des Hauptfensters
    root = tk.Tk()
    root.title("Idle Slayer Auto Clicker")
    root.geometry("300x200+100+2000")

    # Erstellen der Kontrollleuchten
    global autoClickerToggle
    global boxToggle
    global chestHuntToggle
    global bonusLvlToggle
    global rageToggle
    global closeToggle
    global boxDetectet
    global chestHuntDetectet
    global bonusLvlLDetectet
    global bonusLvlRDetectet
    global rageDetectet
    global closeDetectet

    autoClickerToggle = tk.BooleanVar()
    boxToggle = tk.BooleanVar()
    chestHuntToggle = tk.BooleanVar()
    bonusLvlToggle = tk.BooleanVar()
    rageToggle = tk.BooleanVar()
    closeToggle = tk.BooleanVar()
    boxDetectet = tk.BooleanVar()
    chestHuntDetectet = tk.BooleanVar()
    bonusLvlLDetectet = tk.BooleanVar()
    bonusLvlRDetectet = tk.BooleanVar()
    rageDetectet = tk.BooleanVar()
    closeDetectet = tk.BooleanVar()

    checkbox1 = tk.Checkbutton(root, text="Auto Clicker an(t)", variable=autoClickerToggle)
    checkbox1.pack()
    checkbox2 = tk.Checkbutton(root, text="Box", variable=boxToggle)
    checkbox2.pack()
    checkbox2D = tk.Checkbutton(root, text="Box Detectet",variable=boxDetectet)
    checkbox2D.pack()
    checkbox3 = tk.Checkbutton(root, text="Chest Hunt", variable=chestHuntToggle)
    checkbox3.pack()
    checkbox3D = tk.Checkbutton(root,text="Chest Hunt Detectet",variable=chestHuntDetectet)
    checkbox3D.pack()
    checkbox4 = tk.Checkbutton(root, text="Bonus Level", variable=bonusLvlToggle)
    checkbox4.pack()
    checkbox4DL = tk.Checkbutton(root,text="Bonus L Detectet",variable=bonusLvlLDetectet)
    checkbox4DL.pack()
    checkbox4DR = tk.Checkbutton(root,text="Bonus R Detectet",variable=bonusLvlRDetectet)
    checkbox4DR.pack()
    checkbox5 = tk.Checkbutton(root, text="Rage Mode", variable=rageToggle)
    checkbox5.pack()
    checkbox5D = tk.Checkbutton(root,text="Rage Mode Detectet",variable=rageDetectet)
    checkbox5D.pack()
    checkbox6 = tk.Checkbutton(root, text="Close Detection",variable=closeToggle)
    checkbox6
    root.mainloop()


def toggle_event(key):
    if key == TOGGLE_BUTTON:
        global clicking
        if clicking:
            clicking = not clicking
            autoClickerToggle.set(False)
        else:
            clicking = not clicking
            autoClickerToggle.set(True)
    
def detectionT():
    while True:
        if autoClickerToggle.get():
            if boxToggle:
                if det.box(idleWindow):
                    boxDetectet.set(True)
                else:
                    boxDetectet.set(False)
            if chestHuntToggle.get():
                if det.chestHunt(idleWindow):
                    chestHuntDetectet.set(True)
                else:
                    chestHuntDetectet.set(False)
            if bonusLvlToggle.get():
                if det.bonusL(idleWindow):
                    bonusLvlLDetectet.set(True)
                else:
                    bonusLvlLDetectet.set(False)
                if det.bonusR(idleWindow):
                    bonusLvlRDetectet.set(True)
                else:
                    bonusLvlRDetectet.set(False)
            if rageToggle.get():
                if det.rage(idleWindow):
                    rageDetectet.set(True)
                else:
                    rageDetectet.set(False)
            if closeToggle.get():
                if det.bonusClose():
                    closeDetectet.set(True)
                else:
                    closeDetectet.set(False)


def main():
    while True:
        # ON/OFF Condition Key "t"
        if clicking:
            # Detecting Chest Hunt
            if chestHuntDetectet.get():
                saviorX , saviorY = det.savior(idleWindow)
                f.chestHunt(saviorX,saviorY,idleWindow)
                
            # Detecting Box
            if boxDetectet.get():
                f.highJump(700,400)
            # Detecting Bonus Lvl
            elif bonusLvlLDetectet.get():
               f.bonusDrag(idleWindow,"l")
            elif bonusLvlRDetectet.get():
               f.bonusDrag(idleWindow,"r")
            elif det.bonusClose(idleWindow):
               bonusClose = pyautogui.locateCenterOnScreen("assets/bonusClose.png",region=(rootX + 660, rootY+550,150,68),grayscale=True, confidence=0.8 )
               win32api.SetCursorPos((bonusClose.x,bonusClose.y))
               win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
               win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)            
            ## Spam Click
            else:
                #f.jumpShoot(700,400)
                f.shoot(700,400)

                f.boost(700,400)
                       
        time.sleep(0.001)

gui_thread = threading.Thread(target=gui)
gui_thread.start()



main_thread = threading.Thread(target=main)
main_thread.start()

detetction_thread = threading.Thread(target=detectionT)
detetction_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()


