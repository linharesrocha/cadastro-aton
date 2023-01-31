import colorama
from colorama import Fore, Style
import pandas as pd

list_cod = [
'F24822',
'F24722',
'CGRTANTURS',
'GRTANTUCRDD',
'GRTANTUCRDDD',
'GRTANTURSDD',
'BTUNSTTGPT',
'F62',
'F241',
'F243',
'GRTANT1AZ',
'F244',
'P1171',
'KITGRHALGRTANPT',
'P188',
'15175299003',
'GRHALTUCRDD',
'GRQUATUPTDD',
'P215',
'CQDAGTUPTDD'
]

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
