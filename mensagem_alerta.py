#Alertar e pedir informações ao usuário
import pyautogui

#pyautogui.alert(text='iniciando sua automação',title='Automação de login', button='ok')
email = pyautogui.prompt(text='Digite seu e-mail', title='informações obrigatórias')

print(f'Você digitou {email}')