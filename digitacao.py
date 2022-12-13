import pyautogui
import pyperclip

#Função para escrever frase com caracteres especiais.
def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')

# Mover o mouse até o campo de digitar
pyautogui.moveTo(2438,731, duration=2)
# Clicar no campo de digitar
pyautogui.click()
# Digitar minha mensagem
escrever_frase('Olá, bom dia!')
# Clicar no botão de enviar 
pyautogui.click(2690,733, duration=2)