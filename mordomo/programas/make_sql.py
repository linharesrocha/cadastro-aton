import colorama
from colorama import Fore, Style
import pandas as pd

data = pd.read_excel('excel/sku_netshoes.xlsx')

list_cod = data['ID_Sku'].to_list()
print(len(list_cod))
last_element = list_cod[-1]

string_inicial = "WHERE SKU IN("

print(Fore.RED + '\nCÓDIGO PARA O BANCO DE DADOS:')
print(Fore.BLUE + string_inicial, end="")
for cod in list_cod:
    if cod == last_element:
        print("'" + cod + "')")
    else:
        print("'" + cod + "', ", end="")

print(Fore.RED + '\nQUANTIDADE TOTAL DOS DADOS:')
print(Fore.BLUE + str(len(list_cod)))
