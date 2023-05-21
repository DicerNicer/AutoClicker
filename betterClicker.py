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
    root.geometry("300x200+100+1000")

    # Erstellen der Kontrollleuchten
    global var1
    global var2
    global var3
    global var4
    var1 = tk.BooleanVar()
    var2 = tk.BooleanVar()
    var3 = tk.BooleanVar()
    var4 = tk.BooleanVar()

    checkbox1 = tk.Checkbutton(root, text="Auto Clicker an", variable=var1)
    checkbox1.pack()
    checkbox2 = tk.Checkbutton(root, text="Box", variable=var2)
    checkbox2.pack()
    checkbox3 = tk.Checkbutton(root, text="Chest Hunt", variable=var3)
    checkbox3.pack()
    checkbox4 = tk.Checkbutton(root, text="Bonus Level", variable=var4)
    checkbox4.pack()
    root.mainloop()


def toggle_event(key):
    if key == TOGGLE_BUTTON:
        global clicking
        if clicking:
            clicking = not clicking
            var1.set(False)
        else:
            clicking = not clicking
            var1.set(True)
    

def main():
    while True:
        # ON/OFF Condition Key "t"
        if clicking:
            # Detecting Chest Hunt
            if det.chestHunt(idleWindow):
                var3.set(True)
                saviorX , saviorY = det.savior(idleWindow)
                f.chestHunt(saviorX,saviorY,idleWindow)
                
            # Detecting Box
            if det.box(idleWindow):
                var2.set(True)
                print("Box")
                f.highJump(700,400)
            # Detecting Bonus Lvl
            elif det.bonusR(idleWindow):
               var4.set(True)
               print("Bonus")
               f.bonusDrag(idleWindow,"r")
            elif det.bonusL(idleWindow):
               var4.set(True)
               print("Bonus")
               f.bonusDrag(idleWindow,"l")
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
                var2.set(False)
                var3.set(False)
                var4.set(False)                       
        time.sleep(0.001)

gui_thread = threading.Thread(target=gui)
gui_thread.start()

main_thread = threading.Thread(target=main)
main_thread.start()



with Listener(on_press=toggle_event) as listener:
    listener.join()


