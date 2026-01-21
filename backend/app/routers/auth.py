from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from app.db import get_connection
from app.security import verify_password, create_access_token, hash_password

router = APIRouter(prefix='/auth', tags=["auth"])

class LoginRequest(BaseModel):
    username:str = Field(min_length=3, max_length=255)
    password:str = Field(min_length=3, max_length=255)

class LoginResponse(BaseModel):
    access_token:str
    token_type:str = "bearer"

class RegisterRequest(BaseModel):
    username: str = Field(min_length=3, max_length=255)
    password: str = Field(min_length=6, max_length=255)

class RegisterResponse(BaseModel):
    access_token:str
    token_type:str = "bearer"

# Router com prefixo /auth, tipo de resposta: LoginResponse 
@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    username = data.username
    password = data.password
    print("Login : ")
    print("usuario : ", username)
    print("senha : ", password)
    print()
    sql = '''
            select id, password_hash, role
            from dbo.users
            where user_name = ? and is_active = 1
          '''
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(sql, username)
        row = cursor.fetchone()


    if not row or not verify_password(password, row[1]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    
    user_id = row[0]
    role = row[2]

    detail = {
        "user_id": str(user_id),
        "role": role
    }
    token = create_access_token(detail)
    return {"access_token":token, "token_type": "bearer"}
        
@router.post('/register', response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
def register(data: RegisterRequest):
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
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Nome de usuário indisponível")
    
        sql_save_user = '''
                        insert into dbo.users
                        (user_name, password_hash, role, is_active)
                        output inserted.id
                        values(?,?,?,1)
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