import pandas as pd
import warnings
warnings.filterwarnings('ignore')
dados = pd.read_excel('excel/relatorio_magalu_pisste_vendas.xls')

print('Extraindo quantidades de produto')
# Pegando os códigos interno com mais de 1 quantidade no mesmo pedido, e preenchendo no df original
data_h_aux = dados[(dados['QUANT'] > 1)]
data_h_aux['QUANT'] = data_h_aux['QUANT'] - 1
for i in range(len(data_h_aux)):
    pedido = data_h_aux['PEDIDO'].iloc[i]
    cod_interno = data_h_aux['COD_INTERNO'].iloc[i]
    descricao = data_h_aux['DESCRICAOPROD'].iloc[i]
    quantidade = int(data_h_aux['QUANT'].iloc[i])
    sku = data_h_aux['SKU'].iloc[i]
    posicao = data_h_aux['POSICAO'].iloc[i]
    for j in range(quantidade):
        row1 = pd.Series([pedido, cod_interno, descricao, 'INSERT', sku, posicao], index=dados.columns)
        dados = dados.append(row1, ignore_index=True)

dados_result = dados.groupby('SKU').count()
dados_result = dados_result.reset_index()
dados_result.drop(['PEDIDO', 'DESCRICAOPROD', 'COD_INTERNO', 'POSICAO'], axis=1, inplace=True)


data_completo = pd.merge(dados, dados_result, on=['SKU'], how='left')

data_completo.to_excel('excel/REL_VENDAS_MAGALU_PISSTE.xls', index=False)

