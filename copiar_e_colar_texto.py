import pyautogui

pyautogui.click(x=1,y=1,duration=1)
#Selecionar texto
pyautogui.hotkey('ctrl', 'a')
#Copiar texto
pyautogui.hotkey('ctrl', 'c')
#Mover cursor
pyautogui.click(x=1,y=1,duration=1)
#Colar texto
pyautogui.hotkey('ctrl', 'v')