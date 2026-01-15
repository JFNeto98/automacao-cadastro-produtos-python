#Bibliotecas = pacotes de código 
#pip install pyautogui

# Passo a passo do programa
import pyautogui
import time
import pandas
#Variaveis 

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
#Passo 1 Entrar no sistema da empresa
    #Abrir o navegador 

pyautogui.PAUSE = 0.5
pyautogui.press ("win")
pyautogui.write ("Chrome")
pyautogui.press ("enter")

## Selecionar o usario correto do navegador

pyautogui.click(x=873, y=689)
pyautogui.write (link)
pyautogui.press ("enter")
time.sleep (3)


#Passo 2 Fazer o login
## Clicar no campo para o e-mail

pyautogui.click(x=822, y=372)
pyautogui.write ("pythonimpressionador@gmail.com")
pyautogui.press ("tab") ##Passar para o próximo campo
pyautogui.write ("sua senha muito muito dificilima")
pyautogui.press ("tab") ##Passar para o próximo campo
pyautogui.press ("enter")
time.sleep (4) ## Pausa para carregar

#Passo 3 Abrir a base de dados 

tabela = pandas.read_csv("produtos.csv")
print(tabela)

#Passo 4: Cadastrar os produtos

for linha in tabela.index:
    pyautogui.click(x=756, y=263) ##campo do código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press ("tab")
    #Marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press ("tab")

    ##tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press ("tab")

    #Categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press ("tab")

    ##preço unitario 
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press ("tab")

    ##preço custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press ("tab")

    ##OBS
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press ("tab")
    pyautogui.press ("enter")

    ##Scroll na tela 
    pyautogui.scroll(5000)

