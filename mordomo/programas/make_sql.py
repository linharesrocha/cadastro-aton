import colorama
from colorama import Fore, Style

list_cod = [
    '40',
    '47',
    '60',
    '82',
    '85',
    '147',
    '148',
    '150',
    '173',
    '174',
    '265',
    '294',
    '305',
    '315',
    '332',
    '383',
    '408',
    '476',
    '486',
    '532',
    '537',
    '538',
    '561',
    '562',
    '563',
    '567',
    '570',
    '591',
    '595',
    '647',
    '652',
    '656',
    '665',
    '678',
    '679',
    '690',
    '729',
    '744',
    '745',
    '783',
    '828',
    '831',
    '843',
    '848',
    '1010',
    '1014',
    '1017',
    '1038',
    '1045',
    '1092',
    '1093',
    '1097',
    '1110',
    '1135',
    '1139',
    '1164',
    '1169',
    '1224',
    '1242',
    '1285',
    '1301',
    '1303',
    '1306',
    '1307',
    '1309',
    '1310',
    '1311',
    '1312',
    '1313',
    '1314',
    '1315',
    '1428',
    '1440',
    '1441',
    '1442',
    '1482',
]
last_element = list_cod[-1]

string_inicial = "UPDATE MATERIAIS SET INATIVO = 'S' WHERE CODID IN("

print(Fore.RED + '\nCÓDIGO PARA O BANCO DE DADOS:')
print(Fore.BLUE + string_inicial, end="")
for cod in list_cod:
    if cod == last_element:
        print("'" + cod + "')")
    else:
        print("'" + cod + "', ", end="")

print(Fore.RED + '\nQUANTIDADE TOTAL DOS DADOS:')
print(Fore.BLUE +  str(len(list_cod)))