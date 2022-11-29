import pandas as pd

dados = pd.read_excel('excel/deriva_nomes.xls')
print(dados.columns)

listaDerivados = []

for nome in dados['descricao']:
    words_list = nome.split(' ')
    try:
        words_list.remove('DE')
    except ValueError:
        print('')

    listaDerivados.append(' '.join(words_list[:2]))

dados['derivado'] = listaDerivados

dados.to_excel('deriva_nomes_feito.xlsx', index=False)
