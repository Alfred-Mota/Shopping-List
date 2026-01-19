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

def main():
    print("Tentando connectar")
    conexaoDB = pyodbc.connect(CONN_STR, timeout=5)
    print("Connectado")

    cursor = conexaoDB.cursor()
    #Teste direto para verificar conexao
    cursor.execute("select 1")

    #Lendo o retorno imediato do comando
    row = cursor.fetchone()
    print("Teste SELECT 1 retornou: ", row[0])

    conexaoDB.close()
    print("Conexao encerrada")

if __name__ == '__main__':
    main()