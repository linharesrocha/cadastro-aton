import os
from tkinter import *
from tkinter import ttk
import pyperclip
import pyautogui as pg
from time import sleep


def cadastro_basico():
    def program():
        try:
            # Kill Ambar
            os.system("taskkill /im Ambar.exe")
        except:
            print('Ambar não está aberto.')

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
            validation = Label(new1, text="Nome do produto é obrigatório!", bg="red", bd="5", font=24, width=30, height=2)
            validation.place(x=0, y=3)
            return

        if len(codigo_info) == 0:
            validation = Label(new1, text="Código do produto é obrigatório!", bg="red", bd="5", font=24, width=30, height=2)
            validation.place(x=0, y=3)
            return

        if len(ean_info) != 13:
            validation = Label(new1, text="EAN deve conter 13 dígitos.", bg="red", bd="5", font=24, width=30, height=2)
            validation.place(x=0, y=3)
            return

        if len(ncm_info) != 8:
            validation = Label(new1, text="NCM deve conter 8 dígitos.", bg="red", bd="5", font=24, width=30, height=2)
            validation.place(x=0, y=3)
            return

        # Minimiza o Tkinter
        window.iconify()
        new1.iconify()

        # Minimiza todas as abas
        pg.hotkey('winleft', 'd')

        pg.FAILSAFE = False

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
        pg.hotkey('ctrl', 'v')

        # Nome do Produto
        pg.moveTo(905, 316)
        pg.click()
        pyperclip.copy(nome_info)
        pg.hotkey('ctrl', 'v')

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
        listaDescricao = descricao_info.splitlines()

        for frase in listaDescricao:
            pyperclip.copy(frase)
            pg.hotkey('ctrl', 'v')
            pg.hotkey('enter')

        # Botao Salvar
        pg.moveTo(1283, 855)
        # pg.click()

    # Tkinter Config
    new1 = Toplevel(window)
    new1.geometry("1000x900")
    new1.title("Cadastro")

    nome = StringVar()
    codigo = StringVar()
    ean = StringVar()
    peso = StringVar()
    altura = StringVar()
    largura = StringVar()
    comprimento = StringVar()
    ncm = StringVar()

    heading1 = Label(new1, text="Cadastro no Aton", bg="#4682b4", fg="white", width="100", height="2", font=("Helvetica", 16))
    heading1.pack()

    nome_text = Label(new1, text="Nome do Produto")
    codigo_texto = Label(new1, text="Código Interno")
    ean_text = Label(new1, text="EAN")
    peso_text = Label(new1, text="Peso (KG)")
    altura_text = Label(new1, text="Altura")
    largura_text = Label(new1, text="Largura")
    comprimento_text = Label(new1, text="Comprimento")
    ncm_text = Label(new1, text="NCM")
    descricao_text = Label(new1, text="Descricao")

    nome_text.place(x=15, y=70)
    codigo_texto.place(x=15, y=120)
    ean_text.place(x=15, y=170)
    peso_text.place(x=15, y=220)
    altura_text.place(x=15, y=270)
    largura_text.place(x=15, y=320)
    comprimento_text.place(x=15, y=370)
    ncm_text.place(x=15, y=420)
    descricao_text.place(x=15, y=470)

    nome_entry = Entry(new1, textvariable=nome, width=70)
    codigo_entry = Entry(new1, textvariable=codigo)
    ean_entry = Entry(new1, textvariable=ean)
    peso_entry = Entry(new1, textvariable=peso)
    altura_entry = Entry(new1, textvariable=altura)
    largura_entry = Entry(new1, textvariable=largura)
    comprimento_entry = Entry(new1, textvariable=comprimento)
    ncm_entry = Entry(new1, textvariable=ncm)
    descricao_entry = Text(new1)

    nome_entry.place(x=15, y=90)
    codigo_entry.place(x=15, y=140)
    ean_entry.place(x=15, y=190)
    peso_entry.place(x=15, y=240)
    altura_entry.place(x=15, y=290)
    largura_entry.place(x=15, y=340)
    comprimento_entry.place(x=15, y=390)
    ncm_entry.place(x=15, y=440)
    descricao_entry.place(x=15, y=500)

    register = Button(new1, text='Cadastrar', bg="white", fg="black", command=program)
    register.place(x=840, y=850, width=140, height=40)


if __name__ == '__main__':
    # Tkinter Config
    window = Tk()
    window.geometry("500x500")
    window.title("Auxiliar")
    window['background'] = '#778899'

    heading = Label(text="AUXILIAR", bg="#4682b4", fg="white", width="200", height="3", font=("Helvetica", 16))
    heading.pack()

    # Cadastro
    ttk.Button(window, text="CADASTRO BÁSICO ATON", command=cadastro_basico, width=20) \
        .place(x=30, y=110, width=200, height=100)

    # Imagem
    ttk.Button(window, text="IMAGEM PADRÃO", width=20) \
        .place(x=270, y=110, width=200, height=100)

    window.mainloop()
