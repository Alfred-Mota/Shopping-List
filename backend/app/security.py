from datetime import datetime, timedelta
from typing import Optional

from jose import jwt, JWTError
from passlib.context import CryptContext

#===============
#CONFIGURAÇÔES
#===============
SECRET_KEY = "MUDE-ISSO-PARA-ALGO-SEGURO"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Contexto de encriptação
# $2b$12$X9y...sdf -> 
# $2b$ → bcrypt
# 12 → custo (work factor)
# o resto → salt + hash

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#===============
#HASH SENHA
#===============
def hash_password(password:str) -> str:
    return pwd_context.hash(password)

def verify_password(password:str, password_hash:str) -> bool:
    return pwd_context.verify(password, password_hash)

#===============
#JWT CONFIG
#===============

def create_access_token(data:dict, expires_delta:Optional[timedelta] = None)->str:
    to_encode = data.copy()

    expires = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expires})
    print("Token: ", to_encode)
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token:str)->dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
