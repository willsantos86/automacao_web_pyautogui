#Como usar a função click
import pyautogui

# Click personalizado
pyautogui.click(x=1963, y=485,clicks=100, interval=0.1, button='left', duration=2)

# Click na posição atual(com botão esquerdo)
pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='rigth')
pyautogui.click(button='middle')
# Clicar x vezes
pyautogui.click(clicks=10)
# Funções prontas para clicks
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()
pyautogui.tripleClick()