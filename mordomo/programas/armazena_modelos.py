import pyautogui as pg
from time import sleep
import pyperclip
import re
import pandas as pd

pattern = r'[0-9]'


def faz_login_meli():
    pg.moveTo(1166, 179)
    pg.click()

    pg.moveTo(1183, 217)
    pg.click()

    pg.moveTo(1477, 355)
    pg.click()

    pg.typewrite('pedroigor.santana@outlook.com')

    pg.moveTo(1450, 421)
    pg.click()
    sleep(5)


# faz_login_meli()

palavras_poluidas = '''
1. Anilhas (Usada 42 vezes)

2. Kit (Usada 28 vezes)

3. De (Usada 26 vezes)

4. Musculação (Usada 25 vezes)

5. Barras (Usada 20 vezes)

6. E (Usada 18 vezes)

7. Halteres (Usada 17 vezes)

8. Barra (Usada 17 vezes)

9. - (Usada 16 vezes)

10. Para (Usada 16 vezes)

11. Com (Usada 15 vezes)

12. + (Usada 12 vezes)

13. Fitness (Usada 11 vezes)

14. Anilha (Usada 11 vezes)

15. Kg (Usada 10 vezes)

16. Ferro (Usada 10 vezes)

17. P/ (Usada 9 vezes)

18. Prado (Usada 8 vezes)

19. Fundido (Usada 8 vezes)

20. 2 (Usada 7 vezes)
'''


# Limpando as palavras#
# palavras_poluidas = re.sub(pattern, '', palavras_poluidas)

lista_palavras_completa = palavras_poluidas.split('\n')
lista_palavras_completa = list(filter(None, lista_palavras_completa))

lista_palavras_pos = []

aux = 1
for palavra in lista_palavras_completa:
    if aux < 10:
        palavra_numero = palavra[3:].replace(' (Usada', '').replace(' vezes)', '')
    else:
        palavra_numero = palavra[4:].replace(' (Usada', '').replace(' vezes)', '')
    aux = aux + 1

    palavra_numero_lista = palavra_numero.split(' ')
    for word in palavra_numero_lista:
        print(word)