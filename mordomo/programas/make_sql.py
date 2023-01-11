import colorama
from colorama import Fore, Style

list_cod = [
'P672',
'P22',
'P801',
'P800',
'P804',
'P156',
'P710',
'P1417-1',
'P97',
'P214',
'P1416-2',
'P276',
'P252-1',
'P771',
'P396',
'P854',
'P604-1',
'P269-1',
'P773-1',
'P406',
'P405',
'P404',
'P704',
'VVPE7E9FQ',
'AQMEDL6CC',
'P549',
'P87',
'P37',
'P708'
]
last_element = list_cod[-1]

string_inicial = "SELECT * FROM MATERIAIS WHERE CODID IN("

print(Fore.RED + '\nCÓDIGO PARA O BANCO DE DADOS:')
print(Fore.BLUE + string_inicial, end="")
for cod in list_cod:
    if cod == last_element:
        print("'" + cod + "')")
    else:
        print("'" + cod + "', ", end="")

print(Fore.RED + '\nQUANTIDADE TOTAL DOS DADOS:')
print(Fore.BLUE + str(len(list_cod)))
