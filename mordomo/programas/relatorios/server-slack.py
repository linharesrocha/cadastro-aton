import time
import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

SLACK_TOKEN=os.getenv('SLACK_TOKEN')

# Obtenha o token de acesso do bot da variável de ambiente
client = WebClient(token=SLACK_TOKEN)

# ID do canal que você deseja ouvir
channel_id = "C045HEE4G7L"

# Armazena o timestamp da última mensagem que o bot imprimiu
response = client.conversations_history(channel=channel_id, latest=str(time.time()))
lastest_message = response['messages'][0]['text']
latest_timestamp = response["messages"][0]["ts"]

# Adicionando 1 milesimo de segundo
dt = datetime.datetime.fromtimestamp(float(latest_timestamp))
dt += datetime.timedelta(milliseconds=1)
new_timestamp_str = str(dt.timestamp())


def planilha_campanha():
    print('Planilha campanha.')
    subprocess.run(["python", "C:\\workspace\\cadastro-aton\\mordomo\\programas\\relatorios\\sql_server_relatorio_campanha.py"])


while True:
    try:
        # Chamada API para ouvir mensagens do canal a partir do timestamp atual
        response = client.conversations_history(channel=channel_id, oldest=new_timestamp_str)
        
        # Procura a mensagem "campanha" nas mensagens do canal
        for message in response["messages"]:
            if "--campanha" in message["text"].lower():
                # Armazena o timestamp da última mensagem que o bot imprimiu
                response = client.conversations_history(channel=channel_id, latest=str(time.time()))
                lastest_message = response['messages'][0]['text']
                latest_timestamp = response["messages"][0]["ts"]

                # Adicionando 1 milesimo de segundo
                dt = datetime.datetime.fromtimestamp(float(latest_timestamp))
                dt += datetime.timedelta(seconds=1)
                new_timestamp_str = str(dt.timestamp())
                
                # Envia mensagem de aguarde
                response = client.chat_postMessage(text='AU AU!', channel=channel_id)
                
                # Ativa função
                planilha_campanha()


        # Espera 5 segundos antes de buscar novas mensagens
        time.sleep(2)

    except SlackApiError as e:
        print("Erro ao buscar mensagens: {}".format(e))