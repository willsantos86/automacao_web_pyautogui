# Como utilizar botôes e atalhos no teclado
import pyautogui

# Navegar e clicar no campo
pyautogui.click(x=1,y=1,duration=1)
#Digitar o email
pyautogui.typewrite('email.oi@email')
# Apertar tab
pyautogui.press('tab')
# Digitar senha
pyautogui.typewrite('123456')
# Apertar tab
pyautogui.press('tab')
# Apertar space
pyautogui.press('space')

#Nomedas teclas em Inglês
#print(pyautogui.KEYBOARD_KEYS)