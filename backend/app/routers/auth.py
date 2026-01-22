from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.auth import LoginRequest, LoginResponse, RegisterRequest, RegisterResponse
from app.services.auth import login_user, register_user, logout_user
from ..security.test_auth import get_current_user_payload

router = APIRouter(prefix='/auth', tags=["auth"])

# Router com prefixo /auth, tipo de resposta: LoginResponse 
@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    
    token = login_user(data)
    if(token):
        return token
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    
        
@router.post('/register', response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
def register(data: RegisterRequest):
    
    token = register_user(data)
    if token:
        return token
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Usuário indisponível")
        
@router.post('/logout', status_code=status.HTTP_200_OK)
def register(token = Depends(get_current_user_payload)):
    user_id = int(token['sub'])
    res = logout_user(user_id)
    if res:
        return 
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Usuário indisponível")