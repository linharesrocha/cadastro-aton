from tkinter import *
from tkinter import ttk

import pyperclip
from PIL import Image
from tkinter import filedialog as fd
from tkinter import messagebox
from auxiliar import *
from datetime import datetime
import random

# Strings Global
NOME_DO_PRODUTO = '[NOME DO PRODUTO]'
NOME_DO_KIT = '[NOME DO KIT COMPLETO]'

DESCRICAO_INICIAL = 'Receba em sua casa o melhor em qualidade e preço de materiais fitness e academia, ' \
                    'garrafa de água, marmiteiras, bolsas térmicas, Garrafa Termica, e muito mais. Pedidos ' \
                    'realizados antes de 11 horas, serão despachados no mesmo dia! Nós somos excelência em ' \
                    'atendimentos aos nossos clientes, mande suas dúvidas ou perguntas, vamos responder ' \
                    'rápidamente. '

LOGIN_USER = 'GUI'
LOGIN_PASS = '2552'

now = datetime.now()
DATE_TIME = now.strftime("%Y%m%d")

INICIAL_KITDG = 'KITDG'
INICIAL_KIT = 'KIT '

RANDOM = random.randint(0, 9)


def cadastro_basico():
    def program():
        matar_ambar()

        # Pega informações do Cadastro
        nome_info = nome.get()
        codigo_info = codigo.get()
        ean_info = ean.get()
        peso_info = peso.get()
        altura_info = altura.get()
        largura_info = largura.get()
        comprimento_info = comprimento.get()
        ncm_info = ncm.get()
        grupo_info = grupo.get()
        descricao_info = descricao_entry.get("1.0", END)
        autocateogoria_info = autocategoria.get()

        # Validação
        if len(nome_info) == 0:
            validation = Label(new1, text="Nome do produto é obrigatório!", bg="red", bd="5", font=24, width=30,
                               height=2)
            validation.place(x=0, y=3)
            return

        if len(codigo_info) == 0:
            validation = Label(new1, text="Código do produto é obrigatório!", bg="red", bd="5", font=24, width=30,
                               height=2)
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

        minimiza_janelas(window, new1)

        executa_icone_aton()

        login_aton(LOGIN_USER, LOGIN_PASS)

        menu_produtos()

        opcao_cadastro_produtos()

        # Botao Novo
        cadastro_produtos_botao_novo()

        # Código Interno
        cadastro_produtos_codigo_interno()
        pg.typewrite(['backspace', 'backspace', 'backspace', 'backspace'])
        pyperclip.copy(codigo_info)
        pg.hotkey('ctrl', 'v')

        # Nome do Produto
        cadastro_produtos_nome_produto()
        pyperclip.copy(nome_info)
        pg.hotkey('ctrl', 'v')

        # Ean
        cadastro_produtos_ean()
        pg.typewrite(ean_info)

        # Peso
        cadastro_produtos_peso()
        pg.typewrite(peso_info)

        # Altura
        cadastro_produtos_altura()
        pg.typewrite(altura_info)

        # Largura
        cadastro_produtos_largura()
        pg.typewrite(largura_info)

        # Comprimento
        cadastro_produtos_comprimento()
        pg.typewrite(comprimento_info)

        # NCM
        cadastro_produtos_ncm()
        pg.typewrite(ncm_info)

        # Seta do Grupo
        cadastro_produtos_seta_grupo()

        if grupo_info == 'LEAL':
            cadastro_produtos_opcao_grupo_leal()
        if grupo_info == 'MADZ':
            cadastro_produtos_opcao_grupo_madz()
        if grupo_info == 'PISSTE':
            cadastro_produtos_opcao_grupo_pisste()

        # Categoria
        if autocateogoria_info == 1:
            pg.moveTo(878, 591)
            pg.doubleClick()
            pg.moveTo(1228, 421)
            sleep(1.5)
            pg.doubleClick()

        # Descrição
        cadastro_produtos_descricao()
        pyperclip.copy(NOME_DO_PRODUTO)
        pg.hotkey('ctrl', 'v')
        pg.hotkey('enter')
        pg.hotkey('enter')
        pyperclip.copy(DESCRICAO_INICIAL)
        pg.hotkey('ctrl', 'v')
        pg.hotkey('enter')
        pg.hotkey('enter')
        listaDescricao = descricao_info.splitlines()
        for frase in listaDescricao:
            pyperclip.copy(frase)
            pg.hotkey('ctrl', 'v')
            pg.hotkey('enter')

        cadastro_produtos_botao_salvar()

    # Tkinter Config
    new1 = Toplevel(window)
    new1.geometry("1000x950")
    new1.title("Cadastro")

    nome = StringVar()
    codigo = StringVar()
    ean = StringVar()
    peso = StringVar()
    altura = StringVar()
    largura = StringVar()
    comprimento = StringVar()
    ncm = StringVar()
    grupo = StringVar()
    autocategoria = IntVar()

    heading1 = Label(new1, text="Cadastro Simples", bg="#4682b4", fg="white", width="100", height="2",
                     font=("Helvetica", 16))
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
    grupo_text = Label(new1, text="Grupo")

    nome_text.place(x=15, y=70)
    codigo_texto.place(x=15, y=120)
    ean_text.place(x=15, y=170)
    peso_text.place(x=15, y=220)
    altura_text.place(x=15, y=270)
    largura_text.place(x=15, y=320)
    comprimento_text.place(x=15, y=370)
    ncm_text.place(x=15, y=420)
    descricao_text.place(x=15, y=470)
    grupo_text.place(x=200, y=120)

    nome_entry = Entry(new1, textvariable=nome, width=70)
    codigo_entry = Entry(new1, textvariable=codigo)
    ean_entry = Entry(new1, textvariable=ean)
    peso_entry = Entry(new1, textvariable=peso)
    altura_entry = Entry(new1, textvariable=altura)
    largura_entry = Entry(new1, textvariable=largura)
    comprimento_entry = Entry(new1, textvariable=comprimento)
    ncm_entry = Entry(new1, textvariable=ncm)
    descricao_entry = Text(new1, font=('Helvetica', 10), width=100)
    grupo_entry = ttk.Combobox(new1, width=27, textvariable=grupo)
    grupo_entry['values'] = ('LEAL',
                             'MADZ',
                             'PISSTE')
    autocategoria_entry = Checkbutton(new1, text="Vincular categoria automaticamente", variable=autocategoria,
                                      onvalue=1, offvalue=0)

    nome_entry.place(x=15, y=90)
    codigo_entry.place(x=15, y=140)
    ean_entry.place(x=15, y=190)
    peso_entry.place(x=15, y=240)
    altura_entry.place(x=15, y=290)
    largura_entry.place(x=15, y=340)
    comprimento_entry.place(x=15, y=390)
    ncm_entry.place(x=15, y=440)
    descricao_entry.place(x=15, y=500)
    grupo_entry.place(x=200, y=140)
    grupo_entry.current()
    autocategoria_entry.place(x=450, y=90)

    register = Button(new1, text='Cadastrar', bg="white", fg="black", command=program)
    register.place(x=840, y=850, width=140, height=40)


def conversor_imagem():
    file_path = fd.askopenfilename(title='Escolha um arquivo', multiple=True,
                                   filetypes=[('image files', ('.png', '.jpg', '.jpeg',
                                                               '.gif', '.webp', '.tiff',
                                                               '.psd', '.raw', '.bmp',
                                                               '.heif', '.indd'))])
    for path in file_path:
        # Directory
        path_split_list = path.split('/')
        name_original = path_split_list[-1]
        name_split_list = name_original.split('.')
        path_original = path_split_list[:-1]
        path_original = '/'.join(path_original)
        path_original = path_original + '/'

        # Conversion and Save
        pic = Image.open(path)
        pic = pic.resize((1000, 1000))
        pic.convert("RGB").save(path_original + 'novo_' + name_split_list[0] + '.jpg')

        messagebox.showinfo("Pronto!", "Conversão concluida!")


def cadastro_kit():
    def program2():
        matar_ambar()

        codigo_interno_list = []
        nomes_list = []
        descricoes_list = []
        peso_list = []
        altura_list = []
        largura_list = []
        comprimento_list = []

        idaton1_info = idaton1.get()
        idaton2_info = idaton2.get()
        idaton3_info = idaton3.get()
        list_idaton_info = [idaton1_info, idaton2_info, idaton3_info]
        list_idaton_info = list(filter(None, list_idaton_info))
        list_idaton_info = list(map(int, list_idaton_info))

        grupo_info = grupo.get()
        checkbox_altura_info = checkbox_altura.get()
        checkbox_comprimento_info = checkbox_comprimento.get()
        checkbox_largura_info = checkbox_largura.get()

        quantidade1_info = quantidade1.get()
        quantidade2_info = quantidade2.get()
        quantidade3_info = quantidade3.get()
        list_quantidade_info = [quantidade1_info, quantidade2_info, quantidade3_info]
        list_quantidade_info = list(filter(None, list_quantidade_info))
        list_quantidade_info = list(map(int, list_quantidade_info))

        # Validacoes
        if len(list_idaton_info) == 0:
            Label(new3, text="ID do Produto é Obrigatório!", bg="red", bd="5", font=24, width=60,
                  height=2).place(x=0, y=3)
            return

        if len(list_quantidade_info) == 0:
            Label(new3, text="Quantidade é Obrigatório!", bg="red", bd="5", font=24, width=60,
                  height=2).place(x=0, y=3)
            return

        if len(list_idaton_info) == 1:
            if quantidade1_info == '' and quantidade2_info == '' and quantidade3_info == '':
                Label(new3, text="Preencha o campo quantidade!", bg="red", bd="5", font=24, width=60,
                      height=2).place(x=0, y=3)
                return

            if list_quantidade_info[0] < 2 or list_quantidade_info[1] < 2 or list_quantidade_info[2] < 2:
                Label(new3, text="Não é um Kit!", bg="red", bd="5", font=24, width=60,
                      height=2).place(x=0, y=3)
                return

        try:
            if list_idaton_info[0] == list_idaton_info[1] or list_idaton_info[0] == list_idaton_info[2] or list_idaton_info[1] == list_idaton_info[2]:
                Label(new3, text="IDs não podem ser iguais!", bg="red", bd="5", font=24, width=60,
                      height=2).place(x=0, y=3)
                return
        except IndexError:
            pass

        minimiza_janelas(window, new3)

        executa_icone_aton()

        login_aton(LOGIN_USER, LOGIN_PASS)

        menu_produtos()

        opcao_cadastro_produtos()

        cadastro_produtos_botao_consultar()

        consultar_produtos_opcao_todos()

        for idaton in list_idaton_info:
            consultar_produtos_pesquisa()
            pyperclip.copy(idaton)
            pg.hotkey('ctrl', 'v')

            consultar_produtos_botao_consultar()

            consultar_produtos_select_resultado()

            # CODIGO PARA PEGAR INFORMAÇÕES E ARMAZENAR
            cadastro_produtos_botao_alterar()

            cadastro_produtos_codigo_interno()
            pg.hotkey('ctrl', 'a')
            pg.hotkey('ctrl', 'c')
            info = pyperclip.paste()
            codigo_interno_list.append(info)

            cadastro_produtos_nome_produto()
            pg.hotkey('ctrl', 'a')
            pg.hotkey('ctrl', 'c')
            info = pyperclip.paste()
            nomes_list.append(info)

            cadastro_produtos_peso()
            pg.hotkey('ctrl', 'a')
            pg.hotkey('ctrl', 'c')
            info = pyperclip.paste()
            peso_list.append(info.replace(',', '.'))

            cadastro_produtos_altura()
            pg.hotkey('ctrl', 'a')
            pg.hotkey('ctrl', 'c')
            info = pyperclip.paste()
            altura_list.append(info.replace(',', '.'))

            cadastro_produtos_largura()
            pg.hotkey('ctrl', 'a')
            pg.hotkey('ctrl', 'c')
            info = pyperclip.paste()
            largura_list.append(info.replace(',', '.'))

            cadastro_produtos_comprimento()
            pg.hotkey('ctrl', 'a')
            pg.hotkey('ctrl', 'c')
            info = pyperclip.paste()
            comprimento_list.append(info.replace(',', '.'))

            cadastro_produtos_descricao()
            pg.hotkey('ctrl', 'a')
            pg.hotkey('ctrl', 'c')
            info = pyperclip.paste()
            descricoes_list.append(info)

            cadastro_produtos_botao_cancelar()
            cadastro_produtos_botao_consultar()

        # Soma dimensões
        peso_total = str(sum(map(float, peso_list)))
        altura_total = int(sum(map(float, altura_list)))
        largura_total = int(sum(map(float, largura_list)))
        comprimento_total = int(sum(map(float, comprimento_list)))

        altura_maior = int(max(map(float, altura_list)))
        largura_maior = int(max(map(float, largura_list)))
        comprimento_maior = int(max(map(float, comprimento_list)))

        # Criando Produto Kit
        button_close_aton()
        cadastro_produtos_botao_novo()

        # Código Interno
        cadastro_produtos_codigo_interno()
        pg.hotkey('ctrl', 'a')
        pg.press('backspace')
        pyperclip.copy(INICIAL_KITDG)
        pg.hotkey('ctrl', 'c')
        pg.hotkey('ctrl', 'v')
        pg.typewrite(str(DATE_TIME) + str(RANDOM))

        # Nome
        aux = 1
        cadastro_produtos_nome_produto()
        pyperclip.copy(INICIAL_KIT)
        pg.hotkey('ctrl', 'c')
        pg.hotkey('ctrl', 'v')
        for name in nomes_list:
            pyperclip.copy(name)
            pg.hotkey('ctrl', 'v')
            if len(nomes_list) != aux:
                pg.typewrite('+ ')
            aux = aux + 1

        # Peso
        cadastro_produtos_peso()
        pg.typewrite(peso_total)

        # Altura
        cadastro_produtos_altura()
        if checkbox_altura_info == 1:
            pyperclip.copy(altura_total)
            pg.hotkey('ctrl', 'v')
        else:
            pyperclip.copy(altura_maior)
            pg.hotkey('ctrl', 'v')

        # Largura
        cadastro_produtos_largura()
        if checkbox_largura_info == 1:
            pyperclip.copy(largura_total)
            pg.hotkey('ctrl', 'v')
        else:
            pyperclip.copy(largura_maior)
            pg.hotkey('ctrl', 'v')

        # Comprimento
        cadastro_produtos_comprimento()
        if checkbox_comprimento_info == 1:
            pyperclip.copy(comprimento_total)
            pg.hotkey('ctrl', 'v')
        else:
            pyperclip.copy(comprimento_maior)
            pg.hotkey('ctrl', 'v')

        # Seta do Grupo
        cadastro_produtos_seta_grupo()
        if grupo_info == 'LEAL':
            cadastro_produtos_opcao_grupo_leal()
        if grupo_info == 'MADZ':
            cadastro_produtos_opcao_grupo_madz()
        if grupo_info == 'PISSTE':
            cadastro_produtos_opcao_grupo_pisste()

        # Descrição
        cadastro_produtos_descricao()
        pyperclip.copy(NOME_DO_KIT)
        pg.hotkey('ctrl', 'v')
        pg.hotkey('enter')
        pg.hotkey('enter')
        aux = 1
        for descricao in descricoes_list:
            pyperclip.copy(NOME_DO_PRODUTO)
            pg.hotkey('ctrl', 'v')
            pg.typewrite(' ' + str(aux))
            pg.hotkey('enter')
            listaDescricao = descricao.splitlines()
            for frase in listaDescricao:
                pyperclip.copy(frase)
                pg.hotkey('ctrl', 'v')
                pg.hotkey('enter')
            aux = aux + 1

        cadastro_produtos_opcao_desmembra_comp()
        cadastro_produtos_botao_salvar()

        # Salvando Itens Composicao
        cadastro_produtos_aba_composicao()
        aux_quantidade = 0
        for codigo in codigo_interno_list:
            cadastro_produtos_composicao_botao_novo()
            cadastro_produtos_composicao_pesquisa_codigo()
            pg.typewrite(codigo)
            pg.press('enter')
            sleep(1)
            cadastro_produtos_composicao_resultado_produto()
            cadastro_produtos_composicao_quantidade()
            pyperclip.copy(list_quantidade_info[aux_quantidade])
            pg.hotkey('ctrl', 'v')
            aux_quantidade = aux_quantidade + 1
            cadastro_produtos_composicao_botao_salvar()
            sleep(1)

    ############ TKINTER #############
    new3 = Toplevel(window)
    new3.geometry("400x350")
    new3.title("Cadastro")

    idaton1 = StringVar()
    idaton2 = StringVar()
    idaton3 = StringVar()
    quantidade1 = StringVar()
    quantidade2 = StringVar()
    quantidade3 = StringVar()
    grupo = StringVar()
    checkbox_altura = IntVar()
    checkbox_comprimento = IntVar()
    checkbox_largura = IntVar()

    heading3 = Label(new3, text="Cadastro Kit", bg="#4682b4", fg="white", width="100", height="2",
                     font=("Helvetica", 16))
    heading3.pack()

    idaton1_text = Label(new3, text="Código ID Aton - 1")
    idaton2_text = Label(new3, text="Código ID Aton - 2")
    idaton3_text = Label(new3, text="Código ID Aton - 3")
    quantidade_text = Label(new3, text="Quantidade")
    grupo_text = Label(new3, text="Grupo")
    dimensao_text = Label(new3, text="Somar Kits")

    idaton1_text.place(x=140, y=70)
    idaton2_text.place(x=140, y=140)
    idaton3_text.place(x=140, y=210)
    quantidade_text.place(x=280, y=70)
    grupo_text.place(x=25, y=70)
    dimensao_text.place(x=20, y=140)

    idaton1_entry = Entry(new3, textvariable=idaton1)
    idaton2_entry = Entry(new3, textvariable=idaton2)
    idaton3_entry = Entry(new3, textvariable=idaton3)
    quantidade1_entry = Entry(new3, textvariable=quantidade1)
    quantidade2_entry = Entry(new3, textvariable=quantidade2)
    quantidade3_entry = Entry(new3, textvariable=quantidade3)
    grupo_entry = ttk.Combobox(new3, width=27, textvariable=grupo)
    grupo_entry['values'] = ('LEAL',
                             'MADZ',
                             'PISSTE')
    checkbox_altura_entry = Checkbutton(new3, text="Altura", variable=checkbox_altura,
                                        onvalue=1, offvalue=0)
    checkbox_comprimento_entry = Checkbutton(new3, text="Comprimento", variable=checkbox_comprimento,
                                             onvalue=1, offvalue=0)
    checkbox_largura_entry = Checkbutton(new3, text="Largura", variable=checkbox_largura,
                                         onvalue=1, offvalue=0)

    idaton1_entry.place(x=140, y=90)
    idaton2_entry.place(x=140, y=160)
    idaton3_entry.place(x=140, y=230)
    quantidade1_entry.place(x=290, y=90, width=40)
    quantidade2_entry.place(x=290, y=160, width=40)
    quantidade3_entry.place(x=290, y=230, width=40)
    grupo_entry.place(x=25, y=90, width=100)
    grupo_entry.current()
    checkbox_altura_entry.place(x=20, y=160)
    checkbox_comprimento_entry.place(x=20, y=180)
    checkbox_largura_entry.place(x=20, y=200)

    ttk.Button(new3, text="Cadastrar", command=program2, width=20) \
        .place(x=140, y=300, width=120, height=40)


def consulta_produtos_aton():
    matar_ambar()
    minimiza_janelas(window)
    executa_icone_aton()
    login_aton(LOGIN_USER, LOGIN_PASS)
    menu_produtos()
    opcao_cadastro_produtos()


if __name__ == '__main__':
    # Tkinter Config
    window = Tk()
    window.geometry("500x500")
    window.title("Mordomo")
    window['background'] = '#778899'
    window.iconbitmap("icon.ico")
    tabControl = ttk.Notebook(window)

    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)

    heading = Label(text="Mordomo", bg="#4682b4", fg="white", width="200", height="3", font=("Helvetica", 16))
    heading.pack()

    tabControl.add(tab1, text='ATON')
    tabControl.add(tab2, text='AUXILIARES')
    tabControl.add(tab3, text='ATALHOS')
    tabControl.pack(expand=2, fill="both")



    # Cadastro
    ttk.Button(tab1, text="CADASTRO SIMPLES ATON", command=cadastro_basico, width=20) \
        .place(x=30, y=110, width=200, height=100)

    # Imagem
    ttk.Button(tab1, text="CADASTRO KIT ATON", command=cadastro_kit, width=20) \
        .place(x=270, y=110, width=200, height=100)

    # Cadastro Kit
    ttk.Button(tab2, text="CONVERSÃO IMG PADRÃO", command=conversor_imagem, width=20) \
        .place(x=150, y=110, width=200, height=100)

    # Consultar Produtos Aton
    ttk.Button(tab3, text="CONSULTA PRODUTOS ATON", command=consulta_produtos_aton, width=20) \
        .place(x=150, y=110, width=200, height=100)

    window.mainloop()
