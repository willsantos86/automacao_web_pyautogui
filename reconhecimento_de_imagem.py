import pyautogui

#Encontar as cordenadas proximas de onde aquela imagem está
print(pyautogui.locateOnScreen('numero_6.png'))

#Encontar as cordenadas no centro da imagem
print(pyautogui.locateCenterOnScreen('numero_6.png'))

#Como usar na pratica
pyautogui.click(x=1, y=1, duration=1)