import pyautogui

resposta = pyautogui.confirm(text='Continuar rodando nossa automação?', title='confirmação', buttons=['sim', 'não', 'cancelar'])
if resposta == 'sim':
    print('Continuar automação')
elif resposta == 'não':
    print('Encerrando automação')
else:
    print('Operação cancelada')
