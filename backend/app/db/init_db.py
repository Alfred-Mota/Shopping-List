from .connection import get_connection

def init_users_table():
    '''
    Cria a tabela users se ainda não existir
    '''
    #object_id(Nome do objeto, Tipo do Objeto)
    #Nome = users
    #Tipo = User Table -> 'U'
    #identity(seed, increment) -> valor inicial, incremento
    #primary key garante que o atributo é unico e nao pode se repetir, nao pode ser null e é automatico
    sql = """
            if object_id('dbo.users', 'u') is null
            begin
                create table dbo.users(
                id int identity(1,1) primary key,
                user_name nvarchar(255) unique not null,
                password_hash nvarchar(255) not null,
                role nvarchar(50) not null,
                is_active bit not null default 1,
                created_at datetime2 not null default sysdatetime()
            )
            end
         """
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        cursor.commit()
        print("Tabela Users criada")

def init_shopping_items_table():
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
                create table dbo.shopping_items(
                    id int identity(1,1) primary key,
                    item_name nvarchar(255) not null,
                    quantity int not null default 1,
                    created_at datetime2 not null default sysdatetime(),
                    
                    user_id INT NOT NULL,
                    constraint fk_compras_usuario
                        foreign key (user_id)
                        references dbo.users(id)
                        on delete cascade
                )
            end
         """
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql)
        cursor.commit()
        print("Tabela Shopping Items criada")

def init_db():
    init_users_table()
    init_shopping_items_table()