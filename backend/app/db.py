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

def init_db():
    '''
    Cria a tabela shopping_items se ainda não existir
    '''
    #object_id(Nome do objeto, Tipo do Objeto)
    #Nome = shopping_items
    #Tipo = User Table -> 'U'
    #identity(seed, increment) -> valor inicial, incremento
    #primary key garante que o atributo é unico e nao pode se repetir, nao pode ser null e é automatico
    sql = """
            if object_id('dbo.shopping_items', 'u') is null
            begin
                create table shopping_items(
                    id int identity(1,1) primary key,
                    user_name nvarchar(255) not null,
                    item_name nvarchar(255) not null,
                    quantity int not null default 1,
                    created_at datetime2 not null default sysdatetime()
                )
            end
         """
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        cursor.commit()