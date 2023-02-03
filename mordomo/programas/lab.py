import pandas as pd

data1 = pd.read_excel('excel/ATRIB_ML_COLOR_OR_SIZE.xlsx')
data2 = pd.read_excel('excel/TODOS_FILHOS.xlsx')

cor_ou_tamanho_list = []
data1.drop_duplicates(subset='CODID' ,inplace=True)

data_full = pd.merge(data2, data1, how='left',on=['CODID'])
data_full = data_full[data_full['AUTOID'].isna()]
data_full.drop(['AUTOID','TIPO','VALOR','DESCRICAO_y','PRODUTO','SKU','API','IDTIPO','TIPODADO','ALLOW_VARIATIONS','VALOR_ID'], axis=1, inplace=True)

for i in range(len(data_full)):
    name = data_full['DESCRICAO_x'].iloc[i]
    cor_ou_tamanho_list.append('COR') if 'TU' in name else cor_ou_tamanho_list.append('TAMANHO') 

data_full['FALTANTES'] = cor_ou_tamanho_list
data_full.to_excel('excel/PREENCHER_ATRIBUTOS_COR_OU_SIZE.xlsx', index=False)