import pandas as pd
import pyodbc
import datetime
import pandas as pd
import warnings
import numpy as np
import os
import sys
sys.path.append('C:\workspace\cadastro-aton\mordomo\programas')
from db.connect_to_database import get_connection

warnings.filterwarnings('ignore')
os.system('cls')
connection = get_connection()
conexao = pyodbc.connect(connection)
cursor = conexao.cursor()

# Puxa tabela MATERIAIS
