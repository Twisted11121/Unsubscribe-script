import keyboard
import pyautogui
from time import sleep
pyautogui.FAILSAFE = False

while True:
    if keyboard.is_pressed("l") == True:
        pos = pyautogui.position()
        pos1 = pos.x
        pos2 = pos.y + 150

        sleep(0.3)
        pyautogui.click(pos1, pos2)
        sleep(0.2)
        pyautogui.click(1270, 623)
    if keyboard.is_pressed("k") == True:
        quit()
