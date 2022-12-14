'''DESAFIO
1) Vavegue até o site https://www.cursoautomacao.netlify.app/
2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digitar seu nome
3) Clicar em alerta para gerar alerta
4) Feche a  alerta
5) Suba a pagina totalmente para cima
6) Desca apenas o suficiente para conseguir chegar até a secção que contem os arquivos para qual 
você irá fazer o download deles (no caso, você deve fazer essa parte também totalmente com o 
PyAutoGui, nada de trabalho manual aqui) e clicar e movimentar o mouse da maneira que for necessária
para baixar os arquivos de excel e pdf'''

import pyautogui
import webbrowser

webbrowser.open('https://www.cursoautomacao.netlify.app/')