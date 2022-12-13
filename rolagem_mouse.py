import pyautogui
from time import sleep

pyautogui.moveTo(2376,188, duration=2)
for i in range(11):
    pyautogui.scroll(-5)
    sleep(1)