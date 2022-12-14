import pyperclip
from mordomo.auxiliar import *
import pandas as pd

dados = pd.read_excel('excel/madz_faltantes.xlsx')
cod_id_lista = dados['cod_id'].tolist()
tamanho_dados = len(dados)

aux = 1
for id in cod_id_lista:
    print(str(aux) + '/' + str(tamanho_dados))
    # Pesquisa
    pg.moveTo(54, 85)
    pg.click()
    pg.hotkey('ctrl', 'a')
    pg.press('backspace')
    pyperclip.copy(id)
    pg.hotkey('ctrl', 'v')

    # Botao Consultar
    pg.moveTo(776, 81)
    pg.click()
    sleep(1)


    pg.moveTo(1428, 165)
    pg.doubleClick()
    pg.hotkey('ctrl', 'c')
    cabecalho = pyperclip.paste()
    lista_valores_cabecalho = cabecalho.split("\t")
    valor_custo = lista_valores_cabecalho[-3]
    valor_custo = valor_custo.replace(',', '.')

    if valor_custo != '0.00':
        # Markup
        valor = float(valor_custo)
        valor_por = valor * 3
        valor_de = valor * 4

        # Convertendo o preço em uma lista de string
        valor_custo_string_por = str(valor_por)
        valor_custo_string_de = str(valor_de)

        digitos_lista_por = [*valor_custo_string_por]
        digitos_lista_de = [*valor_custo_string_de]

        index_ponto_por = digitos_lista_por.index('.')
        valor_alterar_pre_por = index_ponto_por - 1
        valor_alterar_pos_por = index_ponto_por + 1

        index_ponto_de = digitos_lista_de.index('.')
        valor_alterar_pre_de = index_ponto_de - 1
        valor_alterar_pos_de = index_ponto_de + 1

        # Pegando o segundo digito
        if digitos_lista_por[valor_alterar_pre_por] == '0' or digitos_lista_por[valor_alterar_pre_por] == '5' or \
                digitos_lista_por[
                    valor_alterar_pre_por] == '6' or digitos_lista_por[valor_alterar_pre_por] == '7' or \
                digitos_lista_por[
                    valor_alterar_pre_por] == '8' or digitos_lista_por[valor_alterar_pre_por] == '9':
            digitos_lista_por[valor_alterar_pre_por] = '9'

        if digitos_lista_por[valor_alterar_pre_por] == '1' or digitos_lista_por[valor_alterar_pre_por] == '2' or \
                digitos_lista_por[
                    valor_alterar_pre_por] == '3' or digitos_lista_por[valor_alterar_pre_por] == '4':
            digitos_lista_por[valor_alterar_pre_por] = '4'

        if digitos_lista_de[valor_alterar_pre_de] == '0' or digitos_lista_de[valor_alterar_pre_de] == '5' or \
                digitos_lista_de[
                    valor_alterar_pre_de] == '6' or digitos_lista_de[valor_alterar_pre_de] == '7' or \
                digitos_lista_de[
                    valor_alterar_pre_de] == '8' or digitos_lista_de[valor_alterar_pre_de] == '9':
            digitos_lista_de[valor_alterar_pre_de] = '9'

        if digitos_lista_de[valor_alterar_pre_de] == '1' or digitos_lista_de[valor_alterar_pre_de] == '2' or \
                digitos_lista_de[
                    valor_alterar_pre_de] == '3' or digitos_lista_de[valor_alterar_pre_de] == '4':
            digitos_lista_de[valor_alterar_pre_de] = '4'

        # Alterando o 128.'9'
        digitos_lista_por[valor_alterar_pos_por] = '9'
        digitos_lista_de[valor_alterar_pos_de] = '9'

        valor_por_final = ''.join(digitos_lista_por)
        valor_pre_final = ''.join(digitos_lista_de)

        # Float To String
        valor_por_final = str(valor_por_final).replace('.', ',')
        valor_pre_final = str(valor_pre_final).replace('.', ',')
    else:
        valor_por_final = '0,00'
        valor_pre_final = '0,00'
    84, 99

    # Preenchendo Preço De
    pg.moveTo(1510, 165)
    pg.click()
    pyperclip.copy(valor_pre_final)
    pg.hotkey('ctrl', 'v')

    # Preenche Preço Por
    pg.moveTo(1610, 165)
    pg.click()
    pyperclip.copy(valor_por_final)
    pg.hotkey('ctrl', 'v')
    pg.press('down')

    aux = aux + 1