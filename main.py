from tkinter import *
from tkinter import ttk
from PIL import Image
from tkinter import filedialog as fd
from tkinter import messagebox
from auxiliar import *
from datetime import datetime
import random

# Strings Global
NOME_DO_PRODUTO = '[NOME DO PRODUTO]'

DESCRICAO_INICIAL = 'Receba em sua casa o melhor em qualidade e preço de materiais fitness e academia, ' \
                    'garrafa de água, marmiteiras, bolsas térmicas, Garrafa Termica, e muito mais. Pedidos ' \
                    'realizados antes de 11 horas, serão despachados no mesmo dia! Nós somos excelência em ' \
                    'atendimentos aos nossos clientes, mande suas dúvidas ou perguntas, vamos responder ' \
                    'rápidamente. '

LOGIN_USER = 'GUI'
LOGIN_PASS = '2552'

now = datetime.now()
DATE_TIME = now.strftime("%Y%m%d")

RANDOM = random.randint(0,9)
print(RANDOM)


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

        # # Validação
        # if len(nome_info) == 0:
        #     validation = Label(new1, text="Nome do produto é obrigatório!", bg="red", bd="5", font=24, width=30, height=2)
        #     validation.place(x=0, y=3)
        #     return
        #
        # if len(codigo_info) == 0:
        #     validation = Label(new1, text="Código do produto é obrigatório!", bg="red", bd="5", font=24, width=30, height=2)
        #     validation.place(x=0, y=3)
        #     return
        #
        # if len(ean_info) != 13:
        #     validation = Label(new1, text="EAN deve conter 13 dígitos.", bg="red", bd="5", font=24, width=30, height=2)
        #     validation.place(x=0, y=3)
        #     return
        #
        # if len(ncm_info) != 8:
        #     validation = Label(new1, text="NCM deve conter 8 dígitos.", bg="red", bd="5", font=24, width=30, height=2)
        #     validation.place(x=0, y=3)
        #     return

        minimiza_janelas(new1, window)

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
            pg.moveTo(812, 575)
            pg.click()
        if grupo_info == 'MADZ':
            pg.moveTo(794, 594)
            pg.click()
        if grupo_info == 'PISSTE':
            pg.moveTo(782, 615)
            pg.click()

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
    def conversor():
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

    # Tkinter Config
    new2 = Toplevel(window)
    new2.geometry("300x300")
    new2.title("Cadastro")

    heading2 = Label(new2, text="Conversor de Imagem", bg="#4682b4", fg="white", width="100", height="2",
                     font=("Helvetica", 16))
    heading2.pack()

    ttk.Button(new2, text="Converter", command=conversor, width=20) \
        .place(x=50, y=110, width=200, height=100)


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

        quantidade1_info = quantidade1.get()
        quantidade2_info = quantidade2.get()
        quantidade3_info = quantidade3.get()

        # Só pode cadastrar se tiver mais de 1 ID
        # if len(list_idaton_info) < 2:
        #     return

        minimiza_janelas(new3, window)

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

        # Altera virgula para ponto
        # print(peso_list)
        # print(altura_list)
        # print(largura_list)
        # print(comprimento_list)

        # Soma dimensões
        peso_total = str(sum(map(float, peso_list)))
        print(peso_total)
        # if str(peso_total)[0] == '0':
        #     peso_total = str(peso_total)[:5].replace(',', '.')

        altura_total = int(sum(map(float, altura_list)))
        largura_total = int(sum(map(float, largura_list)))
        comprimento_total = int(sum(map(float, comprimento_list)))

        # Criando Produto Kit
        button_close_aton()
        cadastro_produtos_botao_novo()

        # Código Interno
        cadastro_produtos_codigo_interno()
        pg.hotkey('ctrl', 'a')
        pg.press('backspace')
        pg.typewrite('KITDG' + str(DATE_TIME) + str(RANDOM))

        # Nome
        aux = 1
        cadastro_produtos_nome_produto()
        pg.typewrite('KIT ')
        for name in nomes_list:
            pyperclip.copy(name)
            pg.hotkey('ctrl', 'v')
            if len(nomes_list) != aux:
                pg.typewrite('+ ')
            aux = aux + 1

        if sum((len(i) for i in nomes_list)) > 100:
            messagebox.showinfo("Ops!", "O nome ultrapassou mais de 100 caracteres. Pode haver dado faltando!")

        cadastro_produtos_peso()
        pg.typewrite(peso_total)

        cadastro_produtos_altura()
        pyperclip.copy(altura_total)
        pg.hotkey('ctrl', 'v')

        cadastro_produtos_largura()
        pyperclip.copy(largura_total)
        pg.hotkey('ctrl', 'v')

        cadastro_produtos_comprimento()
        pyperclip.copy(comprimento_total)
        pg.hotkey('ctrl', 'v')



    # Tkinter Config
    new3 = Toplevel(window)
    new3.geometry("400x350")
    new3.title("Cadastro")

    idaton1 = StringVar()
    idaton2 = StringVar()
    idaton3 = StringVar()
    quantidade1 = StringVar()
    quantidade2 = StringVar()
    quantidade3 = StringVar()

    heading3 = Label(new3, text="Cadastro Kit", bg="#4682b4", fg="white", width="100", height="2",
                     font=("Helvetica", 16))
    heading3.pack()

    idaton1_text = Label(new3, text="Código ID Aton - 1")
    idaton2_text = Label(new3, text="Código ID Aton - 2")
    idaton3_text = Label(new3, text="Código ID Aton - 3")
    quantidade_text = Label(new3, text="Quantidade")

    idaton1_text.place(x=140, y=70)
    idaton2_text.place(x=140, y=140)
    idaton3_text.place(x=140, y=210)
    quantidade_text.place(x=280, y=70)

    idaton1_entry = Entry(new3, textvariable=idaton1)
    idaton2_entry = Entry(new3, textvariable=idaton2)
    idaton3_entry = Entry(new3, textvariable=idaton3)
    quantidade1_entry = Entry(new3, textvariable=quantidade1)
    quantidade2_entry = Entry(new3, textvariable=quantidade2)
    quantidade3_entry = Entry(new3, textvariable=quantidade3)

    idaton1_entry.place(x=140, y=90)
    idaton2_entry.place(x=140, y=160)
    idaton3_entry.place(x=140, y=230)
    quantidade1_entry.place(x=290, y=90, width=40)
    quantidade2_entry.place(x=290, y=160, width=40)
    quantidade3_entry.place(x=290, y=230, width=40)

    ttk.Button(new3, text="Cadastrar", command=program2, width=20) \
        .place(x=140, y=300, width=120, height=40)


if __name__ == '__main__':
    # Tkinter Config
    window = Tk()
    window.geometry("500x500")
    window.title("Auxiliar")
    window['background'] = '#778899'

    heading = Label(text="AUXILIAR", bg="#4682b4", fg="white", width="200", height="3", font=("Helvetica", 16))
    heading.pack()

    # Cadastro
    ttk.Button(window, text="CADASTRO SIMPLES ATON", command=cadastro_basico, width=20) \
        .place(x=30, y=110, width=200, height=100)

    # Imagem
    ttk.Button(window, text="CADASTRO KIT ATON", command=cadastro_kit, width=20) \
        .place(x=270, y=110, width=200, height=100)

    # Cadastro Kit
    ttk.Button(window, text="CONVERSÃO IMG PADRÃO", command=conversor_imagem, width=20) \
        .place(x=30, y=280, width=200, height=100)

    window.mainloop()
