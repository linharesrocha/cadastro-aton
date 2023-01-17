import pyautogui as pg
from time import sleep
import pyperclip
import re
import pandas as pd


palavras_poluidas = '''
1. Mochila (Usada 49 vezes)

2. Bolsa (Usada 27 vezes)

3. De (Usada 14 vezes)

4. Feminina (Usada 13 vezes)

5. Kit (Usada 12 vezes)

6. Para (Usada 11 vezes)

7. Viagem (Usada 8 vezes)

8. Maternidade (Usada 7 vezes)

9. Couro (Usada 6 vezes)

10. Escolar (Usada 6 vezes)

11. Masculina (Usada 6 vezes)

12. Notebook (Usada 6 vezes)

13. Impermeável (Usada 5 vezes)

14. Grande (Usada 5 vezes)

15. Trabalho (Usada 4 vezes)

16. Hidratação (Usada 4 vezes)

17. Bebê (Usada 4 vezes)

18. E (Usada 4 vezes)

19. + (Usada 4 vezes)

20. Infantil (Usada 4 vezes)
'''
titulo = f'''
Fone de Ouvido Bluetooth Smartogo Multilaser PH256 In-ear 90db Original
'''

lista_palavras_completa = palavras_poluidas.split('\n')
lista_palavras_completa = list(filter(None, lista_palavras_completa))
termos_list = []
titulo_list_aux = titulo.split(' ')
titulo_list = []
for word in titulo_list_aux:
    word = word.replace('\n', '')
    titulo_list.append(word)


aux = 1
for palavra in lista_palavras_completa:
    if aux < 10:
        palavra_numero = palavra[3:].replace(' (Usada', '').replace(' vezes)', '')
    else:
        palavra_numero = palavra[4:].replace(' (Usada', '').replace(' vezes)', '')
    aux = aux + 1

    palavra_numero_lista = palavra_numero.split(' ')
    termos_list.append(palavra_numero_lista[0])

palavras_set = set(titulo_list)
termos_set = set(termos_list)

diferencas = termos_set - palavras_set

for word in diferencas:
    print(word)

print(' ')