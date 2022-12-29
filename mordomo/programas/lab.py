import pandas as pd
data = pd.read_excel('C:\Ambar\Docs\RelProdutos01.xls')

data['Dt. Ult Saída'] = pd.to_datetime(data['Dt. Ult Saída'], dayfirst=True)
# data['Dt. Ult Saída']= data['Dt. Ult Saída'].dt.strftime('%d-%m-%Y')

data2 = data[(data['Dt. Ult Saída'] <= '2022-11-30') & (data['Estoque Real'] == 0)]

data2.to_excel('Vendas_Ate_Novembro.xls', index=False)