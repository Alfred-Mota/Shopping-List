import os
import pyodbc

# CONN_STR = (
#     "DRIVER={ODBC Driver 17 for SQL Server};"
#     "SERVER=localhost;"
#     "DATABASE=ShoppingDB;"
#     "UID=sa;"
#     "PWD=SuaSenhaAqui;"
# )

# Windows Authentication 
# CONN_STR = (
#     "DRIVER={ODBC Driver 17 for SQL Server};"
#     "SERVER=localhost;"
#     "DATABASE=ShoppingDB;"
#     'Trusted_Connection=yes;'
# )

server = 'DESKTOP-68O9AP5' # Substitua pelo nome do servidor SQL Server
database = 'ShoppingDB'  # Substitua pelo nome do banco de dados

CONN_STR = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f'SERVER={server};'
    f'DATABASE={database};'
    'Trusted_Connection=yes;'
)

def get_connection():
    '''
    Abre e retorna uma conexao pyodbc com o SQL Server
    '''
    return pyodbc.connect(CONN_STR, timeout=5)
