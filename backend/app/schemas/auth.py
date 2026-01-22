from pydantic import BaseModel, Field

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

class LogoutRequest(BaseModel):
    access_token:str
    token_type:str = "bearer"