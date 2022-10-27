import random
from setup import *
from auxiliar import *
from datetime import datetime
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import pyperclip
from PIL import Image

# Strings Global
NOME_DO_PRODUTO = '[NOME DO PRODUTO]'
NOME_DO_KIT = '[NOME DO KIT COMPLETO]'

DESCRICAO_INICIAL = 'Receba em sua casa o melhor em qualidade e preço de materiais fitness e academia, ' \
                    'garrafa de água, marmiteiras, bolsas térmicas, Garrafa Termica, e muito mais. Pedidos ' \
                    'realizados antes de 11 horas, serão despachados no mesmo dia! Nós somos excelência em ' \
                    'atendimentos aos nossos clientes, mande suas dúvidas ou perguntas, vamos responder ' \
                    'rápidamente. '

now = datetime.now()
DATE_TIME = now.strftime("%Y%m%d")

INICIAL_KITDG = 'KITDG'
INICIAL_KIT = 'KIT '


def cadastro_basico():
    def program():

        # Pega informações do Cadastro
        nome_info = nome.get()
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

        if len(ean_info) != 13:
            validation = Label(new1, text="EAN deve conter 13 dígitos.", bg="red", bd="5", font=24, width=30, height=2)
            validation.place(x=0, y=3)
            return

        if len(ncm_info) != 8:
            validation = Label(new1, text="NCM deve conter 8 dígitos.", bg="red", bd="5", font=24, width=30, height=2)
            validation.place(x=0, y=3)
            return

        matar_ambar()

        minimiza_janelas(window, new1)

        executa_icone_aton()

        login_aton()

        menu_produtos()

        opcao_cadastro_produtos()

        # Botao Novo
        cadastro_produtos_botao_novo()

        # Código Interno
        codigo_ean_montagem = ["DG", ean_info[0], ean_info[8:]]
        codigo_ean_montagem = list(map(str, codigo_ean_montagem))
        codigo_ean_final = ''.join(codigo_ean_montagem)
        cadastro_produtos_codigo_interno()
        pyperclip.copy(codigo_ean_final)
        pg.typewrite(['backspace', 'backspace', 'backspace', 'backspace'])
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
        cadastro_produtos_seta_grupo(grupo_info)

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
    codigo_entry = Entry(new1, state='disabled')
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
        pic = pic.resize((1000, 1000), Image.Resampling.LANCZOS)
        pic.convert("RGB").save(path_original + 'novo_' + name_split_list[0] + '.jpg')

        messagebox.showinfo("Conversão concluida!", "A imagem foi salva no mesmo diretório da imagem original!")


def gerador_cod_interno():
    def program():
        ean_codigo_info = ean_codigo_entry.get("1.0", END)
        lista_de_ean = ean_codigo_info.splitlines()
        lista_de_ean = list(filter(None, lista_de_ean))

        aux = 1.0
        for ean in lista_de_ean:
            if len(ean) != 13:
                validation = Label(new4, text="EAN deve conter 13 dígitos.", bg="red", bd="5", font=24, width=80, height=2)
                validation.place(x=0, y=3)
                return

            # Transformando no padrão
            codigo_ean_montagem = ["DG", ean[0], ean[8:]]
            codigo_ean_montagem = list(map(str, codigo_ean_montagem))

            # Junta a lista em um código único
            codigo_ean_final = ''.join(codigo_ean_montagem)

            # Apagando o que está escrito, e inserindo o código depois
            ean_codigo_final_entry.insert(END, codigo_ean_final + '\n')

    def limpar():
        ean_codigo_final_entry.delete("1.0", "end")

    ############ TKINTER #############
    new4 = Toplevel(window)
    new4.geometry("600x580")
    new4.title("Gerador")

    ean_codigo = StringVar()

    heading3 = Label(new4, text="Gerador Código Interno", bg="#4682b4", fg="white", width="100", height="2",
                     font=("Helvetica", 16))
    heading3.pack()

    ean_codigo_text = Label(new4, text="Digite o código EAN")
    ean_codigo_entry = Text(new4, font=('Helvetica', 10), width=30)
    ean_codigo_text.place(x=110, y=70)
    ean_codigo_entry.place(x=70, y=90)

    ean_codigo_final_text = Label(new4, text="Resultado")
    ean_codigo_final_entry = Text(new4, font=('Helvetica', 10), width=30)
    ean_codigo_final_text.place(x=390, y=70)
    ean_codigo_final_entry.place(x=320, y=90)

    ttk.Button(new4, text="Gerar", command=program, width=20) \
        .place(x=70, y=470, width=215, height=40)

    ttk.Button(new4, text="Limpar", command=limpar, width=20) \
        .place(x=320, y=470, width=215, height=40)


def gerador_cod_interno_kit():
    def program():
        RANDOM = random.randint(0, 99)
        codigo_final = INICIAL_KITDG + str(DATE_TIME) + str(RANDOM)
        ean_codigo_final_entry.delete(0, 'end')
        ean_codigo_final_entry.insert(0, codigo_final)
        return codigo_final

    def copiar():
        pyperclip.copy(ean_codigo_final_entry.get())

    ############ TKINTER #############
    new4 = Toplevel(window)
    new4.geometry("400x250")
    new4.title("Gerador Código Kit")

    heading3 = Label(new4, text="Gerador Código Interno Kit", bg="#4682b4", fg="white", width="100", height="2",
                     font=("Helvetica", 16))
    heading3.pack()

    ttk.Button(new4, text="Gerar", command=program, width=20) \
        .place(x=140, y=70, width=120, height=40)

    ean_codigo_final_text = Label(new4, text="Resultado")
    ean_codigo_final_text.place(x=140, y=160)

    ean_codigo_final_entry = Entry(new4)
    ean_codigo_final_entry.place(x=140, y=180, height=40)

    ttk.Button(new4, text="Copiar", command=copiar, width=20) \
        .place(x=310, y=180, width=60, height=30)


def abrir_garantia():
    def program():
        pedido_aton_info = pedido_aton.get()
        pedido_loja_info = pedido_loja.get()
        pedido_esc_info = pedido_esc.get()
        quantidade_produto_info = quantidade_produto.get()
        checkbox_garantia_info = checkbox_garantia.get()
        checkbox_produto_unico_info = checkbox_produto_unico.get()
        motivo_info = motivo.get()


        # Validações
        # Obrigar a pessoa colocar um das três pesquisas


        matar_ambar()

        minimiza_janelas(window, new5)

        executa_icone_aton()

        login_aton()

        entrar_na_tela_f8()

        f8_botao_limpar()

        if pedido_aton_info != '':
            print('oi')
        if pedido_loja_info != '':
            print('oi')
        if pedido_esc_info != '':
            print('oi')

    def enable_produto_unico():
        checkbox_produto_unico_entry.config(state="active")

    def enable_quantidade():
        quantidade_produto_entry.config(state="normal")
    ############ TKINTER #############

    new5 = Toplevel(window)
    new5.geometry("550x300")
    new5.title("Abrir Garantia")

    pedido_aton = StringVar()
    pedido_loja = StringVar()
    pedido_esc = StringVar()
    quantidade_produto = StringVar()
    checkbox_garantia = IntVar()
    checkbox_produto_unico = IntVar()
    motivo = StringVar()

    heading3 = Label(new5, text="Abrir Garantia", bg="#4682b4", fg="white", width="100", height="2",
                     font=("Helvetica", 16))
    heading3.pack()

    pedido_aton_text = Label(new5, text="Pedido Aton")
    pedido_loja_text = Label(new5, text="Pedido Loja")
    pedido_esc_text = Label(new5, text="Pedido ESC")
    quantidade_produto_text = Label(new5, text="Quantidade")
    motivo_text = Label(new5, text="Motivo")

    pedido_aton_text.place(x=40, y=70)
    pedido_loja_text.place(x=40, y=140)
    pedido_esc_text.place(x=40, y=210)
    quantidade_produto_text.place(x=360, y=140)
    motivo_text.place(x=220, y=140)

    pedido_aton_entry = Entry(new5, textvariable=pedido_aton)
    pedido_loja_entry = Entry(new5, textvariable=pedido_loja)
    pedido_esc_entry = Entry(new5, textvariable=pedido_esc)
    checkbox_garantia_entry = Checkbutton(new5, text="Abrir Garantia?", variable=checkbox_garantia, onvalue=1,
                                          offvalue=0, command=enable_produto_unico)

    checkbox_produto_unico_entry = Checkbutton(new5, text="Produto único?", variable=checkbox_produto_unico,  onvalue=1,
                                                   offvalue=0, state='disabled', command=enable_quantidade)
    quantidade_produto_entry = Entry(new5, textvariable=quantidade_produto, state='disabled')
    motivo_entry = ttk.Combobox(new5, width=45, textvariable=motivo)
    motivo_entry['values'] = ('DESISTENCIA 7D',
                              'END. INCORRETO',
                              'GARANTIA',
                              'PROD C/ DEFEITO',
                              'PROD DIVERGENTE',
                              'PROD FALTANTE',
                              'PROD QUEBRADO',
                              'RECUSADO',
                              'AO REMETENTE')

    pedido_aton_entry.place(x=40, y=90)
    pedido_loja_entry.place(x=40, y=160)
    pedido_esc_entry.place(x=40, y=230)
    quantidade_produto_entry.place(x=360, y=160, width=40)
    checkbox_garantia_entry.place(x=215, y=90)
    checkbox_produto_unico_entry.place(x=360, y=90)
    motivo_entry.place(x=220, y=160, width=100)
    motivo_entry.current()

    ttk.Button(new5, text="Aplicar", command=program, width=20) \
        .place(x=230, y=220, width=260, height=40)


def cadastro_kit():
    def program2():
        matar_ambar()

        codigo_interno_list = []
        nomes_list = []
        descricoes_list = []
        peso_list = []

        codigointerno1_info = codigointerno1.get()
        codigointerno2_info = codigointerno2.get()
        codigointerno3_info = codigointerno3.get()
        list_codigointerno_info = [codigointerno1_info, codigointerno2_info, codigointerno3_info]
        list_codigointerno_info = list(filter(None, list_codigointerno_info))

        grupo_info = grupo.get()

        quantidade1_info = quantidade1.get()
        quantidade2_info = quantidade2.get()
        quantidade3_info = quantidade3.get()
        list_quantidade_info = [quantidade1_info, quantidade2_info, quantidade3_info]
        list_quantidade_info = list(filter(None, list_quantidade_info))
        list_quantidade_info = list(map(int, list_quantidade_info))

        # Validacoes
        if len(list_codigointerno_info) == 0:
            Label(new3, text="ID do Produto é Obrigatório!", bg="red", bd="5", font=24, width=60,
                  height=2).place(x=0, y=3)
            return

        if len(list_quantidade_info) == 0:
            Label(new3, text="Quantidade é Obrigatório!", bg="red", bd="5", font=24, width=60,
                  height=2).place(x=0, y=3)
            return

        if len(list_codigointerno_info) == 1:
            if quantidade1_info == '' and quantidade2_info == '' and quantidade3_info == '':
                Label(new3, text="Preencha o campo quantidade!", bg="red", bd="5", font=24, width=60,
                      height=2).place(x=0, y=3)
                return

            if list_quantidade_info[0] < 2 or list_quantidade_info[1] < 2 or list_quantidade_info[2] < 2:
                Label(new3, text="Não é um Kit!", bg="red", bd="5", font=24, width=60,
                      height=2).place(x=0, y=3)
                return

        try:
            if list_codigointerno_info[0] == list_codigointerno_info[1] or list_codigointerno_info[0] == \
                    list_codigointerno_info[2] or \
                    list_codigointerno_info[1] == list_codigointerno_info[2]:
                Label(new3, text="IDs não podem ser iguais!", bg="red", bd="5", font=24, width=60,
                      height=2).place(x=0, y=3)
                return
        except IndexError:
            pass

        minimiza_janelas(window, new3)

        executa_icone_aton()

        login_aton()

        menu_produtos()

        opcao_cadastro_produtos()

        cadastro_produtos_botao_consultar()

        consultar_produtos_opcao_todos()

        aux = 0
        for codigointerno in list_codigointerno_info:
            consultar_produtos_pesquisa()
            pyperclip.copy(codigointerno)
            pg.hotkey('ctrl', 'v')

            consultar_produtos_botao_consultar()

            # Ordenando apenas uma vez
            if aux != 1:
                consultar_produtos_menu_cod_id()
                aux = aux + 1

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

            cadastro_produtos_descricao()
            pg.hotkey('ctrl', 'a')
            pg.hotkey('ctrl', 'c')
            info = pyperclip.paste()
            descricoes_list.append(info)

            cadastro_produtos_botao_cancelar()
            cadastro_produtos_botao_consultar()

        # Soma Peso
        peso_total = str(sum(map(float, peso_list)))

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
        RANDOM = random.randint(0, 99)
        pg.typewrite(str(DATE_TIME) + str(RANDOM))

        # Nome
        aux = 1
        cadastro_produtos_nome_produto()
        pyperclip.copy(INICIAL_KIT)
        pg.hotkey('ctrl', 'c')
        pg.hotkey('ctrl', 'v')
        aux2 = 0
        for name in nomes_list:
            pyperclip.copy(list_quantidade_info[aux2])
            pg.hotkey('ctrl', 'v')
            pg.press('space')
            pyperclip.copy(name)
            pg.hotkey('ctrl', 'v')
            if len(nomes_list) != aux:
                pg.typewrite('+ ')
            aux = aux + 1
            aux2 = aux2 + 1

        # Peso
        cadastro_produtos_peso()
        pg.typewrite(peso_total)

        # Seta do Grupo
        cadastro_produtos_seta_grupo(grupo_info)

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

    codigointerno1 = StringVar()
    codigointerno2 = StringVar()
    codigointerno3 = StringVar()
    quantidade1 = StringVar()
    quantidade2 = StringVar()
    quantidade3 = StringVar()
    grupo = StringVar()

    heading3 = Label(new3, text="Cadastro Kit", bg="#4682b4", fg="white", width="100", height="2",
                     font=("Helvetica", 16))
    heading3.pack()

    codigointerno1_text = Label(new3, text="Código Interno - 1")
    codigointerno2_text = Label(new3, text="Código Interno - 2")
    codigointerno3_text = Label(new3, text="Código Interno - 3")
    quantidade_text = Label(new3, text="Quantidade")
    grupo_text = Label(new3, text="Grupo")
    dimensao_text = Label(new3, text="Somar Kits")

    codigointerno1_text.place(x=140, y=70)
    codigointerno2_text.place(x=140, y=140)
    codigointerno3_text.place(x=140, y=210)
    quantidade_text.place(x=280, y=70)
    grupo_text.place(x=25, y=70)
    dimensao_text.place(x=20, y=140)

    codigointerno1_entry = Entry(new3, textvariable=codigointerno1)
    codigointerno2_entry = Entry(new3, textvariable=codigointerno2)
    codigointerno3_entry = Entry(new3, textvariable=codigointerno3)
    quantidade1_entry = Entry(new3, textvariable=quantidade1)
    quantidade2_entry = Entry(new3, textvariable=quantidade2)
    quantidade3_entry = Entry(new3, textvariable=quantidade3)
    grupo_entry = ttk.Combobox(new3, width=27, textvariable=grupo)
    grupo_entry['values'] = ('LEAL',
                             'MADZ',
                             'PISSTE')

    codigointerno1_entry.place(x=140, y=90)
    codigointerno2_entry.place(x=140, y=160)
    codigointerno3_entry.place(x=140, y=230)
    quantidade1_entry.place(x=290, y=90, width=40)
    quantidade2_entry.place(x=290, y=160, width=40)
    quantidade3_entry.place(x=290, y=230, width=40)
    grupo_entry.place(x=25, y=90, width=100)
    grupo_entry.current()

    ttk.Button(new3, text="Cadastrar", command=program2, width=20) \
        .place(x=140, y=300, width=120, height=40)


def consulta_produtos_aton():
    matar_ambar()
    minimiza_janelas(window)
    executa_icone_aton()
    login_aton()
    menu_produtos()
    opcao_cadastro_produtos()
    cadastro_produtos_botao_consultar()
    consultar_produtos_opcao_todos()
    consultar_produtos_botao_consultar()


if __name__ == '__main__':
    # Tkinter Config
    window = Tk()
    window.geometry("500x500")
    window.title("Mordomo")
    window['background'] = '#778899'
    # window.iconbitmap("C:\workspace\cadastro-aton\\favicon.ico")
    tabControl = ttk.Notebook(window)

    # Aton
    tab1 = ttk.Frame(tabControl)

    # Auxiliares
    tab2 = ttk.Frame(tabControl)

    # Atalhos
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

    # Abrir Garantia
    ttk.Button(tab1, text="ABRIR GARANTIA", command=abrir_garantia, width=20) \
        .place(x=30, y=240, width=200, height=100)

    # Consultar Produtos Aton
    ttk.Button(tab1, text="CONSULTAR PRODUTOS ATON", command=consulta_produtos_aton, width=20) \
        .place(x=280, y=340, width=210, height=50)

    # Cadastro Kit
    ttk.Button(tab2, text="CONVERSÃO IMG PADRÃO", command=conversor_imagem, width=20) \
        .place(x=30, y=110, width=200, height=100)

    # Gerador COD. Interno
    ttk.Button(tab2, text="GERAR COD. SIMPLES", command=gerador_cod_interno, width=20) \
        .place(x=30, y=250, width=160, height=50)

    # Gerador COD. Interno KIT
    ttk.Button(tab2, text="GERAR COD. KIT", command=gerador_cod_interno_kit, width=20) \
        .place(x=270, y=250, width=160, height=50)

    # Consultar Produtos Aton
    ttk.Button(tab3, text="CONSULTAR PRODUTOS ATON", command=consulta_produtos_aton, width=20) \
        .place(x=30, y=110, width=210, height=100)

    # Consultar Produtos Aton
    ttk.Button(tab3, text="MATAR ATON", command=matar_ambar, width=20) \
        .place(x=270, y=110, width=200, height=100)

    window.mainloop()
