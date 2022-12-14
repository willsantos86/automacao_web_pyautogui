import pyautogui

captcha = pyautogui.locateCenterOnScreen('gogle1.png')
pyautogui.click(captcha[0], captcha[1], duration=2)