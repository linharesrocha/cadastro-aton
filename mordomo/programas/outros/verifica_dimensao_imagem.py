import requests
from PIL import Image
import sys
import pandas as pd
from io import BytesIO
sys.path.append('C:\workspace\cadastro-aton\mordomo\programas')
from db.connect_to_database import *

connection = get_connection()
conexao = pyodbc.connect(connection)
cursor = conexao.cursor()

comando = f'''
SELECT A.AUTOID, A.CODID, B.DESCRICAO, A.URL 
FROM MATERIAIS_IMAGENS A
LEFT JOIN MATERIAIS B
ON A.CODID = B.CODID
WHERE A.CODID > 0
AND B.INATIVO = 'N'
'''

dimensao_list = []
test_list = []
data = pd.read_sql(comando, conexao)

for i in range(len(data)):
    print(f'{str(i)} / {str(len(data))}')
    url = data['URL'][i]

    print(url)
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url
    print(url)
        
    response = requests.get(url)
    
    # Tenta apenas se o link estiver funcionando
    try:
        img = Image.open(BytesIO(response.content))
        width, height = img.size
        dimensao = f'{str(width)}x{str(height)}'
        dimensao_list.append(dimensao)
        
        # Regra para o ERRO
        if width != 1000 and height != 1000 and width != 1200 and height != 1200:
            test_list.append('ERROR')
            print(width)
            print(height)
        else:
            test_list.append('OK')
    except:
        dimensao_list.append('LINK_OFF')
        test_list.append('LINK_OFF')

data['DIMENSAO'] = dimensao_list
data['CHECK'] = test_list
data.to_excel('test.xlsx', index=False)