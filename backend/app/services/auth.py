from ..db.connection import get_connection
from app.security.security import verify_password, create_access_token, hash_password
from app.schemas.auth import LoginRequest, LoginResponse, RegisterRequest, RegisterResponse

def login_user(data: LoginRequest)->LoginResponse:
    username = data.username
    password = data.password
    print("Login : ")
    print("usuario : ", username)
    print("senha : ", password)
    print()
    sql = '''
        update dbo.users
        set is_active = 0
        output inserted.id, inserted.password_hash, inserted.role
        where user_name = ? and is_active = 1
    '''
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql, username)
        row = cursor.fetchone()

        print("ROW: ", row)

    if not row or not verify_password(password, row[1]):
        return False
    
    user_id = row[0]
    role = row[2]

    detail = {
        "user_id": str(user_id),
        "role": role
    }
    token = create_access_token(detail)
    return {"access_token":token, "token_type": "bearer"}
        
def register_user(data: RegisterRequest)->RegisterResponse:
    username = data.username
    password = data.password
    print("Cadastro de novo usuario : ")
    print("usuario : ", username)
    print("senha : ", password)
    print()
    sql_check = "select 1 from dbo.users where user_name = ?"
    
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql_check, username)
        row = cursor.fetchone()

        if row :
            return False
    
        sql_save_user = '''
                        insert into dbo.users
                        (user_name, password_hash, role, is_active)
                        output inserted.id
                        values(?,?,?,0)
                        '''
        password_hash = hash_password(password)
        role = "user"
        cursor.execute(sql_save_user, username, password_hash,role)
        id = cursor.fetchone()[0]
        cursor.commit()

    detail = {
        "user_id": str(id),
        "role": role
    }
    token = create_access_token(detail)
    return {"access_token":token, "token_type": "bearer"}

def logout_user(user_id : int):
    
    print("Logout : ")
    print("usuario : ", user_id)
    print()

    sql = '''
        update dbo.users
        set is_active = 1
        output inserted.id
        where user_name = ? and is_active = 0
    '''
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql, user_id)
        row = cursor.fetchone()
    
    if row:
        return True
    
    return False
