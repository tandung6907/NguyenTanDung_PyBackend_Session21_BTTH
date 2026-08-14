from pydantic import BaseModel, EmailStr

class RegisterInput(BaseModel):
    email       : EmailStr
    password    : str

class LoginInput(BaseModel):
    email       : EmailStr
    password    : str

class AuthResponse(BaseModel):
    access_token: str
    token_type  : str = "bearer"