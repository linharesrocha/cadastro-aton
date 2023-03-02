import requests
import json

# Autenticação
client_id = 'seu-client-id'
client_secret = 'seu-client-secret'
tenant_id = 'seu-tenant-id'
access_token_url = 'https://login.microsoftonline.com/{}/oauth2/v2.0/token'.format(tenant_id)
scope = 'https://graph.microsoft.com/.default'

response = requests.post(access_token_url, data={
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': scope
})

access_token = response.json()['access_token']

# Configuração da chamada API
url = 'https://graph.microsoft.com/v1.0/drives/SEU_DRIVE_ID/items/SEU_ITEM_ID/workbook/worksheets/SEU_NOME_PLANILHA/range(address=SEU_ENDERECO)'
headers = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'}

# Define o endereço do range que deseja apagar os dados
endereco = {'address': 'A1:Z100'}

# Define o payload da chamada para apagar os dados do range
payload = {'values': [[]]}

# Realiza a chamada API para apagar os dados do range
response = requests.patch(url, headers=headers, data=json.dumps(payload))

# Verifica se a chamada foi realizada com sucesso
if response.status_code == 200:
    print('Os dados foram apagados com sucesso.')
else:
    print('Não foi possível apagar os dados.')
