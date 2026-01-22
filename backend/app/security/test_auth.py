from fastapi import Depends, HTTPException, status, Header
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from app.security.security import decode_token

# Metodo automatico para fazer uma leitura do header em busca da Authorization Bearer.
# Abstrai o seguinte trecho
# auth = request.headers.get("Authorization")
# if not auth:
#     raise 401
# if not auth.startswith("Bearer "):
#     raise 401
# token = auth.replace("Bearer ", "")

##Dependes é tipo um middlewer, esta aplicando um metodo e retornando o valor   

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="authorization")

def get_current_user_payload(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        return decode_token(token)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")