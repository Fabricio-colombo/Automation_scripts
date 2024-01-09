import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 2

#abrir a janela win
pyautogui.click(x=531, y=1057)

#digitar o navegador
pyautogui.write('chrome')

#entrar no navegador
pyautogui.press('enter')

#clicar no meu login
pyautogui.click(x=630, y=610)

#clicar no buscador
pyautogui.click(x=264, y=82)

#digitar o site  /  https://dlp.hashtagtreinamentos.com/python/intensivao/login
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)

#entrar no site
pyautogui.press('enter')
time.sleep(3)

#preencher email
pyautogui.click(x=689, y=509)
email = 'fabriciocolombo0096@gmail.com'
pyautogui.write(email)

#preencher senha
pyautogui.press('tab')
senha = 'fabricio12345'
pyautogui.write(senha)
pyautogui.press('tab')
pyautogui.press('enter')

#formularios
tabela = pd.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:

    #preencher
    pyautogui.click(x=655, y=368)

    #codigo
    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')

    #marca
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')

    #tipo
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')

    #categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    #preco_unitario
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    #custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    #obs
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(obs)
        
    pyautogui.press('tab')

    #enviar
    pyautogui.press('enter')
    
    #retornar para cima
    pyautogui.scroll(2000)