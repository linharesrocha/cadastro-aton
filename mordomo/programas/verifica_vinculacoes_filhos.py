from mordomo.main import *
from mordomo.auxiliar import *
import pandas as pd


# Verificar se todas descrições estão no padrão

dados = pd.read_excel('excel/verifica_vinculacoes_filhos.xls')
pd.set_option('mode.chained_assignment', None)

# Você precisa entrar no cadastro de produtos
tamanho_planinha = len(dados)


for i in range(tamanho_planinha):
    print(str(i) + '/' + str(tamanho_planinha) + ' -- ' + dados['Descrição'][i] + ' -- ' + dados['Código Interno'][i])
    consultar_produtos_pesquisa()
    pyperclip.copy(dados['Código Interno'][i])
    pg.hotkey('ctrl', 'v')
    consultar_produtos_botao_consultar()
    consultar_produtos_select_resultado()
    cadastro_produtos_aba_variacao()

    check = 'Nao'
    while check != 'S':
        pg.moveTo(2583, 1004)
        pg.click()
        check = input('Corrigido? (S): ')
        check = check.replace(' ', '')
        check = check.upper()
    print(' ')

    cadastro_produtos_aba_cadastro_produtos()
    cadastro_produtos_botao_consultar()