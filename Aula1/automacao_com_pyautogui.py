import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)


pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

#clica no campo de email
pyautogui.click(x=955, y=511)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") #passa pro próximo campo
pyautogui.write("123456789")
pyautogui.click(x=955, y=716) #clica no botao login
time.sleep(3)


tabela = pd.read_csv("produtos.csv")

for linha in tabela.index: #cadastra produtos
    #clicar no campo código
    pyautogui.click(x=814, y=365)
    #pega na tabela o valor do campo que irá preencher
    codigo = tabela.loc[linha, "codigo"]
    #preenche o campo
    pyautogui.write(str(codigo))
    #passa pro proximo campo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") #clica em enviar
    #volta pro inicio da página (vai pra cima)
    pyautogui.scroll(5000)
