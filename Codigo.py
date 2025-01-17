# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

import pyautogui
import time
import pandas

#muda o tempo  de cada comando
pyautogui.PAUSE = 0.3

# 1° Abrir o navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# 2° Entrar no link de login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#pedir para o programa esperar 3 segundos/ import time para o comando abaixo
time.sleep(3)


# 3° Fazer Login 

# selecionar campo email com o codigo pegar posição na outra guia
pyautogui.click(x=766, y=361)

pyautogui.write("iasmim.teste@gmail.com")
pyautogui.press("tab")

pyautogui.write("iasmimlinda")
pyautogui.press("enter")

# 4° Importar dados 

tabela = pandas.read_csv("produtos.csv")
print(tabela)

time.sleep(2)

# 5° Cadastrar um item para teste 



for linha in tabela.index:

    pyautogui.click(x=822, y=237)

    # codigo
    codigo = tabela.loc[1,"codigo"]
    pyautogui.write("MOLO000251")
    pyautogui.press("tab")
    pyautogui.write("Logitech")
    pyautogui.press("tab")
    pyautogui.write("Mouse")
    pyautogui.press("tab")
    pyautogui.write("1")
    pyautogui.press("tab")
    pyautogui.write("25.95")
    pyautogui.press("tab")
    pyautogui.write("6.50")
    pyautogui.press("tab")
    pyautogui.write("")
    pyautogui.press("tab")
    pyautogui.press("enter")

    # scroll negavito pra baixo, scroll positivo pra cima

    pyautogui.scroll(-1000)

    time.sleep(2)
    pyautogui.scroll(10000)

