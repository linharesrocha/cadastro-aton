import openai
import os
import os
from pathlib import Path
import pandas as pd
import sys
from dotenv import load_dotenv
import warnings
import pyodbc
sys.path.append('C:\workspace\cadastro-aton\mordomo\programas')
from db.connect_to_database import get_connection

# Configurações do Programa
warnings.filterwarnings('ignore')
os.system('cls')
connection = get_connection()
conexao = pyodbc.connect(connection)
cursor = conexao.cursor()
env_path = Path('.') / 'C:\workspace\cadastro-aton\mordomo\programas\.env'
load_dotenv(dotenv_path=env_path)
openai.api_key = os.environ['OPENAI_KEY']

# Configurações ChatGPT
def obter_resposta(pergunta):
    prompt = f"Q: {pergunta}\nA:"
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt, 
        temperature=0.5,
        max_tokens=4050,
    )
    return response.choices[0].text.strip()


# Importando tabela de MATERIAIS
comando = f'''
SELECT CODID, COD_INTERNO, DESCRICAO, DESCRITIVO
FROM MATERIAIS
WHERE INATIVO = 'N'
AND DESMEMBRA = 'N'
AND DESCRITIVO IS NOT NULL
'''
df_materiais = pd.read_sql(comando, conexao)

# Percorrendo e obtendo as descrições
for i in range(len(df_materiais)):
    codid = df_materiais['CODID'][i]
    descricao = df_materiais['DESCRICAO'][i]
    descritivo = df_materiais['DESCRITIVO'][i]
    
    # Removendo Frases
    descritivo = descritivo.replace('ENVIO IMEDIATO - PRONTA ENTREGA - NOTA FISCAL - TESTADO - COM GARANTIA','')
    descritivo = descritivo.replace('Prezado cliente, caso possua alguma dúvida, será um prazer lhe atender.','')
    descritivo = descritivo.replace('SOBRE O PRODUTO:','')
    descritivo = descritivo.replace('Todos os produtos são testados, analisados, garantindo mais confiabilidade com a melhor qualidade e preço.','')
    descritivo = descritivo.replace('Somos excelência em atendimento aos nossos clientes. Envie suas dúvidas ou perguntas, de preferência em nosso chat.','')
    descritivo = descritivo.replace('Somos excelência em atendimento aos nossos clientes. Envie suas dúvidas ou perguntas, de preferência em nosso chat.','')
    descritivo = descritivo.replace('ENVIO IMEDIATO - PRONTA ENTREGA - COM NOTA FISCAL - TESTADO - COM GARANTIA','')
    descritivo = descritivo.replace('Nossos produtos estão a pronta entrega e sempre são despachados em até um dia útil, garantindo agilidade no processo de compra.','')
    descritivo = descritivo.replace('Todos os produtos são testados, analisados e possuem nota fiscal, garantindo mais confiabilidade com a melhor qualidade e preço, além disso caso haja alguma inconformidade com o produto basta nos acionar que resolveremos.','')
    descritivo = descritivo.replace('Temos o cuidado de embalar os produtos individualmente, com material de proteção de alta qualidade, certificando que o pedido chegue até ao seu destino intacto, minimizando possíveis danos durante o transporte.','')
    descritivo = descritivo.replace('Somos uma empresa referência no ecommerce, atuamos há mais de 6 anos no ramo. Buscamos muito além de vender produtos, queremos ser o seu maior parceiro e te proporcionar a melhor experiência de compra possível, para quem deseja encontrar produtos de qualidade e ter uma experiência de compra excelente. Seja onde for, teremos orgulho em fazer parte disso. Se inspire e transforme sua vida, juntos somos gigantes!','')
    descritivo = descritivo.replace('Nossos produtos estão a pronta entrega e sempre são despachados em até um dia útil, garantindo agilidade no processo de compra e uma boa experiência para o cliente.','')
    descritivo = descritivo.replace('Nós somos excelência em atendimentos aos nossos clientes, envie suas dúvidas ou perguntas, de preferência em nosso chat, atenderemos com agilidade e empenho para resolver da melhor maneira','')
    check_descritivo = descritivo.split('\n')[0]
    if len(check_descritivo) < 105:
        linhas = descritivo.split('\n')
        nova_descricao = '\n'.join(linhas[1:])
        descritivo = nova_descricao.strip()


    # Perguntando ao ChatGPT
    pergunta = f'''
    
    '''

    if len(pergunta.strip()) > 1:
        resposta = obter_resposta(pergunta)
        os.system('cls')
        print(f'DAGG: {pergunta}\n')
        print(f'GPT: {resposta}\n')
    else:
        print('Digite alguma coisa.')