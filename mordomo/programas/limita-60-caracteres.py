import pyperclip
import pandas as pd
import os
from pathlib import Path
import pyodbc
import pandas as pd
import warnings
from datetime import datetime, date, timedelta
from dotenv import load_dotenv


string_description = 'Mini Bola De Exercícios 25cm Fitness Com Canudo Para Inflar Yoga Pilates'
string_final_list = []
count = 0
aux = 0
if len(string_description) > 60:
    string_list = string_description.split(' ')
    for string in string_list:
        count = count + len(string) + 1
        if count <= 60:
            string_final_list.append(string)
        else:
            count = count - 1
            if count <= 60:
                string_final_list.append(string)
            else:
                break

    string_final = ' '.join(string_final_list)
    if len(string_final) > 60:
        string_final_list = string_final.split(' ')
        string_final_list.pop()
        string_final = ' '.join(string_final_list)
    print(string_final)