import pandas as pd
import pyodbc
import pandas as pd
import warnings
import sys
sys.path.append('C:\workspace\cadastro-aton\mordomo\programas')
from db.connect_to_database import get_connection

connection = get_connection()
conexao = pyodbc.connect(connection)
cursor = conexao.cursor()
data = pd.read_excel('C:\workspace\cadastro-aton\mordomo\programas\excel\ADICIONAR_COR.xlsx')

warnings.filterwarnings('ignore')
for i in range(len(data)):
    # Pega o código id do produto
    codid = data['CODID'].iloc[i]
    
    # Pega o atributo que será preenchdio no VALOR
    atributo = data['VALUE'].iloc[i]

    # Atributo id que será preenchido no IDTIPO
    atributoid = 'COLOR'
    
    # Contagem
    print(str(i) + '/' + str(len(data)))
    print(f'{codid} / {atributo} / {atributoid}')
    
    break
    # Executar comando de inserção de dados na tabela MATERIAIS_ESPECIFICACOES
    comando = f'''INSERT INTO MATERIAIS_ESPECIFICACOES(CODID, TIPO, VALOR,PRODUTO, SKU, API, IDTIPO, ALLOW_VARIATIONS, VALOR_ID) VALUES ('{codid}', '{atributo}', '', 'N', 'N', 'Mercado Livre', '{atributoid}', 'S', '')'''
    cursor.execute(comando)
    conexao.commit()
    
del conexao