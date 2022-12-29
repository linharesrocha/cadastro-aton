from mordomo.main import *
from mordomo.auxiliar import *
from pathlib import Path
from dotenv import load_dotenv
import os
import pandas as pd
import pyodbc

# SLACK SETUP
# env_path_sql = Path('.') / '.env-sql'
# load_dotenv(dotenv_path=env_path_sql)
# DATABASE = os.environ['DATABASE']
# UID = os.environ['UID']
# PWD = os.environ['PWD']
#
# dados_conexao = ("Driver={SQL Server};"
#                  "Server=erp.ambarxcall.com.br;"
#                  "Database=" + DATABASE + ";"
#                                           "UID=" + UID + ";"
#                                                          "PWD=" + PWD + ";")
#
# conexao = pyodbc.connect(dados_conexao)
# cursor = conexao.cursor()
# print("Conexão com o Banco de Dados Bem Sucedida!")
#
# comando = f'''
#     SELECT * FROM MATERIAIS
#     WHERE PAI = 0
#     '''

# dados = pd.read_sql(comando, conexao)
# tamanho_planilha = len(dados)

list_cod = [
    'DG309902PAI',
    'DG309957PAI',
    'DG309993PAI',
    'DG310000',
    'DG310018PAI',
    'DG310123PAI',
    'DG310215PAI',
    'DG310239PAI',
    'DG305629PAI'
    ]

tamanho_planilha = len(list_cod)

aux = 1
for cod in list_cod:
    print(str(aux) + '/' + str(tamanho_planilha) + ' -- ' + cod)
    aux = aux + 1
    consultar_produtos_pesquisa()
    pyperclip.copy(cod)
    pg.hotkey('ctrl', 'v')
    consultar_produtos_botao_consultar()
    sleep(2)
    consultar_produtos_select_resultado()
    cadastro_produtos_aba_ficha_tecnica()
    pg.moveTo(541, 413)
    pg.rightClick()
    pg.moveTo(619, 434)
    pg.click()
    pg.moveTo(648, 337)
    pg.click()
    pg.moveTo(959, 321)
    pg.click()
    # PRIMEIRO
    pg.moveTo(686, 351)
    pg.click()
    pg.moveTo(687, 351)
    pg.click()
    start = 367
    pg.moveTo(1018, 337)
    pg.doubleClick()
    for i in range(40):
        if start < 591:
            pg.moveTo(687, start)
            pg.click()
            start = start + 16
            pg.moveTo(1018, 337)
            pg.doubleClick()

        if start == 591:
            pg.moveTo(687, 576)
            pg.click()
            pg.moveTo(1018, 337)
            pg.doubleClick()
            sleep(0.5)
            start = 591

    # salvando
    pg.moveTo(1139, 751)
    pg.click()
    sleep(1)
    cadastro_produtos_aba_cadastro_produtos()
    cadastro_produtos_botao_consultar()
