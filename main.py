import os
from tkinter import *
import pyperclip
import pyautogui
import pyautogui as pg
from time import sleep


def program():
    # Kill Ambar
    os.system("taskkill /im Ambar.exe")

    # Pega informações do Cadastro
    nome_info = nome.get()
    codigo_info = codigo.get()
    ean_info = ean.get()
    peso_info = peso.get()
    altura_info = altura.get()
    largura_info = largura.get()
    comprimento_info = comprimento.get()
    ncm_info = ncm.get()
    descricao_info = descricao_entry.get("1.0", END)

    # Validação
    if len(nome_info) == 0:
        validation = Label(text="Nome do produto é obrigatório!", bg="red", bd="5", font=24, width=100)
        validation.place(x=0, y=0)
        return

    if len(codigo_info) == 0:
        validation = Label(text="Código do produto é obrigatório!", bg="red", bd="5", font=24, width=100)
        validation.place(x=0, y=0)
        return

    if len(ean_info) != 13:
        validation = Label(text="EAN deve conter 13 dígitos.", bg="red", bd="5", font=24, width=100)
        validation.place(x=0, y=0)
        return

    if len(ncm_info) != 8:
        validation = Label(text="NCM deve conter 8 dígitos.", bg="red", bd="5", font=24, width=100)
        validation.place(x=0, y=0)
        return

    # Minimiza o Tkinter
    window.iconify()

    # Minimiza todas as abas
    pg.hotkey('winleft', 'd')

    pyautogui.FAILSAFE = False

    # Icone do Aton
    pg.moveTo(36, 100)
    pg.doubleClick()

    sleep(1)

    # Campo de Usuário
    pg.moveTo(1583, 532)
    pg.click()
    pg.typewrite('GUI')

    # Campo de Senha
    pg.moveTo(1606, 563)
    pg.click()
    pg.typewrite('2552')

    # Botão de Login
    pg.moveTo(1550, 601)
    pg.doubleClick()

    sleep(5)

    # Menu Produtos
    pg.moveTo(283, 37)
    pg.click()

    # Cadastro de produtos
    pg.moveTo(328, 60)
    pg.click()

    sleep(2)

    # Botao Novo
    pg.moveTo(519, 853)
    pg.click()

    # Código Interno
    pg.moveTo(681, 261)
    pg.click()
    pg.typewrite(['backspace', 'backspace', 'backspace', 'backspace'])
    pyperclip.copy(codigo_info)
    pyautogui.hotkey('ctrl', 'v')

    # Nome do Produto
    pg.moveTo(905, 316)
    pg.click()
    pyperclip.copy(nome_info)
    pyautogui.hotkey('ctrl', 'v')

    # Ean
    pg.moveTo(1143, 261)
    pg.click()
    pg.typewrite(ean_info)

    # Peso
    pg.moveTo(533, 370)
    pg.click()
    pg.typewrite(peso_info)

    # Altura
    pg.moveTo(622, 368)
    pg.click()
    pg.typewrite(altura_info)

    # Largura
    pg.moveTo(719, 367)
    pg.click()
    pg.typewrite(largura_info)

    # Comprimento
    pg.moveTo(817, 370)
    pg.click()
    pg.typewrite(comprimento_info)

    # NCM
    pg.moveTo(541, 423)
    pg.click()
    pg.typewrite(ncm_info)

    # Descrição
    pg.moveTo(633, 684)
    pg.click()
    pyperclip.copy(descricao_info)
    pyautogui.hotkey('ctrl', 'v')

    # Botao Salvar
    pg.moveTo(1283, 855)
    # pg.click()


if __name__ == '__main__':
    # Tkinter Config
    window = Tk()
    window.geometry("1000x900")
    window.title("Cadastro")

    nome = StringVar()
    codigo = StringVar()
    ean = StringVar()
    peso = StringVar()
    altura = StringVar()
    largura = StringVar()
    comprimento = StringVar()
    ncm = StringVar()

    heading = Label(text="Cadastro no Aton", bg="grey", fg="black", width="200", height="3")
    heading.pack()

    nome_text = Label(text="Nome do Produto")
    codigo_texto = Label(text="Código Interno")
    ean_text = Label(text="EAN")
    peso_text = Label(text="Peso (KG)")
    altura_text = Label(text="Altura")
    largura_text = Label(text="Largura")
    comprimento_text = Label(text="Comprimento")
    ncm_text = Label(text="NCM")
    descricao_text = Label(text="Descricao")

    nome_text.place(x=15, y=70)
    codigo_texto.place(x=15, y=120)
    ean_text.place(x=15, y=170)
    peso_text.place(x=15, y=220)
    altura_text.place(x=15, y=270)
    largura_text.place(x=15, y=320)
    comprimento_text.place(x=15, y=370)
    ncm_text.place(x=15, y=420)
    descricao_text.place(x=15, y=470)

    nome_entry = Entry(textvariable=nome, width=70)
    codigo_entry = Entry(textvariable=codigo)
    ean_entry = Entry(textvariable=ean)
    peso_entry = Entry(textvariable=peso)
    altura_entry = Entry(textvariable=altura)
    largura_entry = Entry(textvariable=largura)
    comprimento_entry = Entry(textvariable=comprimento)
    ncm_entry = Entry(textvariable=ncm)
    descricao_entry = Text()

    nome_entry.place(x=15, y=90)
    codigo_entry.place(x=15, y=140)
    ean_entry.place(x=15, y=190)
    peso_entry.place(x=15, y=240)
    altura_entry.place(x=15, y=290)
    largura_entry.place(x=15, y=340)
    comprimento_entry.place(x=15, y=390)
    ncm_entry.place(x=15, y=440)
    descricao_entry.place(x=15, y=500)

    register = Button(window, text='Cadastrar', bg="gray", fg="black", command=program)
    register.place(x=205, y=450)

    window.mainloop()
