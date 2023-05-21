import pyautogui
import win32api, win32con
import detection
import time
#idleWindow = pyautogui.getWindowsWithTitle("Idle Slayer")[0]
#rootX = idleWindow.left
#rootY = idleWindow.top
# firstChestX = idleWindow.left + 220
# firstChestY = idleWindow.top + 500
# win32api.SetCursorPos((firstChestX+95*8,firstChestY))
# print(firstChestX+95*8,firstChestY)
# print(detection.savior(idleWindow))
#iml = pyautogui.screenshot(region=(rootX + 150, rootY+250,1000,300))
#iml.save(r"C:\Users\Sebastian\Documents\Eigene Dokumente\Code\AutoClicker\savedimage.png")

win32api.SetCursorPos((700,400))
i = 0
while(i<6):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    i+=1
    time.sleep(0.001)
    
# print(detection.savior(idleWindow))
# print(detection.chestHunt(idleWindow))