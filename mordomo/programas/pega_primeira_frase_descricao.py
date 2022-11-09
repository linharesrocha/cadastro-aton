import pandas as pd


dados = pd.read_excel('descricao.xls')
quantidade_produtos = len(dados)
descritivo_lista = dados['descricao'].tolist()
primeiro_nome = []
for descritivo in descritivo_lista:
    titulo_descricao = descritivo.splitlines()[0]
    primeiro_nome.append(titulo_descricao)

aux = 0

for nome in primeiro_nome:
    if nome.isupper():
        nome = nome.title()
        print(nome)
        primeiro_nome[aux] = nome
    aux = aux + 1

# dados['nome'] = primeiro_nome
# dados.to_excel('convertido.xlsx', index=False)