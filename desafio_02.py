# DESAFIO  
'''Crie um programa que pede o usuário e senha, e na sequencia, copia e cola
o usuário e senha dentro de um bloco de notas'''

import pyautogui

# Digitar usuário
email = pyautogui.prompt(text='Digite seu e-mail', title='informações obrigatórias')
# Digitar senha
senha = pyautogui.password(text='digite sua senha:', title= 'dados de login', mask='*')
# Mover para o whats
pyautogui.click(2417,736, duration=2)
# Clicar na caixa de mensagem
pyautogui.typewrite(email)
#Pressionar botão enter
pyautogui.press('enter')
# Colar senha e usuário
pyautogui.typewrite(senha)
# Mover e clicar em enviar
pyautogui.click(2452,729, duration=2)
