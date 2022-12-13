from mordomo.auxiliar import *
import pandas as pd
import pyperclip

dados = pd.read_excel('excel/coloca_preco_custo_faltantes.xlsx')
tamanho_planinha = len(dados)


for i in range(tamanho_planinha):
    custo_produto = str(dados['CUSTO'][i])
    print(str(i) + '/' + str(tamanho_planinha) + ' -- ' + dados['Descrição'][i] + ' -- ' + custo_produto)
    print(' ')
    consultar_produtos_pesquisa()
    pyperclip.copy(dados['Código Interno'][i])
    pg.hotkey('ctrl', 'v')
    consultar_produtos_botao_consultar()
    consultar_produtos_select_resultado()
    cadastro_produtos_botao_alterar()
    cadastro_produtos_valor_custo()
    pg.typewrite(custo_produto)
    cadastro_produtos_botao_salvar()
    cadastro_produtos_botao_consultar()