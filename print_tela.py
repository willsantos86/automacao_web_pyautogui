# Como tirar print da tela inteira
import pyautogui
#Print tela inteira
pyautogui.screenshot('tela.jpg')

#Print de uma parte da tela
pyautogui.screenshot('calculadora.jpg', region=(869,130, 200, 400))