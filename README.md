# 🤖 Automação de Cadastro de Produtos com Python (RPA)

Este projeto consiste em uma **automação de processos operacionais (RPA)** desenvolvida em Python para **automatizar o cadastro de produtos em um sistema web**, utilizando uma base de dados estruturada em CSV.

A automação simula a interação humana com a interface gráfica do sistema, reduzindo tarefas manuais repetitivas, erros operacionais e aumentando a eficiência do processo.

---

## 🎯 Objetivo do Projeto

- Automatizar o cadastro de produtos em um sistema web  
- Reduzir esforço manual e retrabalho  
- Garantir padronização no preenchimento dos dados  
- Demonstrar conhecimentos práticos em **Python, RPA e automação de processos**

---

## 🧰 Tecnologias Utilizadas

- **Python**
- **PyAutoGUI** – Automação da interface gráfica
- **Pandas** – Leitura e manipulação de dados
- **Time** – Controle de pausas e sincronização

---

## 🧠 Lógica da Automação (Explicação do Código)

### 1️⃣ Importação das bibliotecas

```python Abertura do navegador e acesso ao sistema
import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

pyautogui.click(x=873, y=689)
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

Login automatizado no sistema

pyautogui.click(x=822, y=372)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha muito muito dificilima")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(4)

Leitura da base de dados (CSV)

tabela = pandas.read_csv("produtos.csv")
print(tabela)

Loop de cadastro dos produtos

for linha in tabela.index:
    pyautogui.click(x=756, y=263)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")


Tratamento de valores nulos

obs = str(tabela.loc[linha, "obs"])
if obs != "nan":
    pyautogui.write(obs)


Envio do formulário e ajuste da tela

pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.scroll(5000)


