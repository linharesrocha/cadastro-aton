import pandas as pd
import pyodbc
import datetime
import pandas as pd
import warnings
import numpy as np
import os
import sys
sys.path.append('C:\workspace\cadastro-aton\mordomo\programas')
from db.connect_to_database import get_connection

warnings.filterwarnings('ignore')
os.system('cls')
connection = get_connection()
conexao = pyodbc.connect(connection)
cursor = conexao.cursor()

# Perguntar ao usuario o grupo dos produtos
comando = f'''
SELECT CODIGO, DESCRICAO 
FROM GRUPO
'''
df_grupo = pd.read_sql(comando, conexao)
print(df_grupo.to_string(index=False))
while True:
    grupo_id = input('\nQual GRUPO de Produtos será adicionado nas publicações?: ')
    if grupo_id.isdigit():
        num = int(grupo_id)
        if num == 3 or num == 4 or num == 6 or num == 7:
            break

# Pergunta se vai publicar KIT
while True:
    publica_kit = input('\nVai publicar Kit (S/N): ').lower()
    if publica_kit == 's' or publica_kit == 'n':
        break

# Verificar Kit e Puxa tabela MATERIAIS
if publica_kit == 's':
    comando = f'''
    SELECT *
    FROM MATERIAIS
    WHERE INATIVO = 'N'
    AND GRUPO = '{grupo_id}'
    '''
else:
    comando = f'''
    SELECT *
    FROM MATERIAIS
    WHERE INATIVO = 'N'
    AND GRUPO = '{grupo_id}'
    AND DESMEMBRA = 'N'
    '''
df_materiais = pd.read_sql(comando, conexao) 

# Pegando ORIGEM_ID
comando = f'''
SELECT ORIGEM_ID, ORIGEM_NOME
FROM ECOM_ORIGEM
'''
df_ecom_origem = pd.read_sql(comando, conexao)
print('\n\n' + df_ecom_origem.to_string(index=False))
while True:
    origem_id = input('\nPara qual marketplace será publicado?: ')
    if origem_id.isdigit():
        num = int(origem_id)
        if num >= 1 and num <= 33:
            break

# Comando para criar produto na publicação
for i in range(len(df_materiais)):
    codid = df_materiais['CODID'][i]
    cod_interno = str(df_materiais['COD_INTERNO'][i]).strip()
    descricao = str(df_materiais['DESCRICAO'][i]).strip()
    valor_custo = str(df_materiais['VLR_CUSTO'][i])
    
    # Código para formar o SKU
    check_pai = int(df_materiais['PAI'][i])
    if check_pai == 0:
        sku = 'P' + str(codid)
    else:
        sku = 'F' + str(codid)

    
    # Inserção de produto
    comando = f'''INSERT INTO PUBLICA_PRODUTO (DATATH, ORIGEM_ID, CODID, SKU, COD_INTERNO, TITULO, ESTOQUE, VLR_CUSTO, VALOR1, VALOR2, USR, MAQSYS, STATUSCODE, FLAG, FLAG_VALIDACAO, USR_PUBLICOU, FRETE_GRATIS, OFICIAL_STORE, OFICIAL_STORE_ID, LEVAEAN, CATALOGO_PRODUTO_ID)
    VALUES (CONVERT(datetime, GETDATE(), 120),'{origem_id}', '{codid}', '{sku}', '{cod_interno}','{descricao}', '1', '{valor_custo}','10', '10', '239', 'DAGG-005', '0', '-9', '0', '0', 'N', '', '0','S', '')'''
    
    # cursor.execute(comando)
    # conexao.commit()
    
    print(f'{str(i + 1)}/{str(len(df_materiais))} - {codid} - {cod_interno} - {descricao}')

print('\nProdutos inserido na publicação com sucesso!\n')

print('\nPreenchendo Coluna PAI e AUTOIDPAI\n')

# Pegando a tabela PUBLICA_PRODUTO antes da publicação
comando = f'''
SELECT *
FROM PUBLICA_PRODUTO
WHERE FLAG = '-9'
AND ORIGEM_ID = '{origem_id}'
AND USR = '239'
'''
df_pre_publicacao = pd.read_sql(comando, conexao)
df_pre_publicacao = df_pre_publicacao[['AUTOID', 'AUTOIDPAI', 'CODID', 'PAI']]
# Pegando outra planilha Materiais
comando = f'''
SELECT CODID, PAI
FROM MATERIAIS
WHERE INATIVO = 'N'
AND GRUPO = '{grupo_id}'
'''
df_materiais_aux = pd.read_sql(comando, conexao)

# Renomeando colunas
df_materiais_aux.rename({'CODID':'MATERIAL_ID', 'PAI':'CODID'})

# Mesclando
df_pre_publicacao = df_pre_publicacao.merge(df_materiais_aux, on='CODID')
df_pre_publicacao.rename(columns={'PAI_y':'PAI_ATUALIZADO', 'PAI_x':'PAI_ANTIGO'}, inplace=True)
df_pre_publicacao.drop(['PAI_ANTIGO'], axis=1, inplace=True)
df_pre_publicacao = df_pre_publicacao[df_pre_publicacao['PAI_ATUALIZADO'] != 0]

# Inserindo PAI nas colunas
for i in range(len(df_pre_publicacao)):
    codid = df_pre_publicacao['CODID'].iloc[i]
    pai = df_pre_publicacao['PAI_ATUALIZADO'].iloc[i]    
    
    # Substitui o PRECO DE
    comando = f'''
    UPDATE PUBLICA_PRODUTO
    SET PAI = '{pai}'
    WHERE CODID = '{codid}'
    AND FLAG = '-9'
    '''
    # cursor.execute(comando)
    # conexao.commit()

print('\nAdicionado código pai nos filhos com sucesso!\n')

# Adicionando AUTOIDPAI nos filhos

# Lendo novamente publicar anúncio após atualização
comando = f'''
SELECT *
FROM PUBLICA_PRODUTO
WHERE FLAG = '-9'
AND ORIGEM_ID = '{origem_id}'
AND USR = '239'
'''
df_publicacao_anuncio = pd.read_sql(comando,conexao)

# percorre cada linha do DataFrame
for index, row in df_publicacao_anuncio.iterrows():

    # verifica se o valor do pai é maior que 0
    if row["PAI"] > 0:

        # filtra o DataFrame para encontrar a linha correspondente ao valor PAI
        pai = row["PAI"]
        filtro = df_publicacao_anuncio[df_publicacao_anuncio["CODID"] == pai]

        # verifica se o filtro retornou alguma linha
        if not filtro.empty:

            # busca o valor correspondente na coluna AUTOID
            autoid_pai = filtro["AUTOID"].iloc[0]

            # atualiza a coluna AUTOIDPAI com o valor correspondente do AUTOID
            df_publicacao_anuncio.at[index, "AUTOIDPAI"] = autoid_pai
        
print('\nAdicionado autoidpai nos filhos com sucesso!\n')