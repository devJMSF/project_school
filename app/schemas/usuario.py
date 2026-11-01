from pydantic import BaseModel, Field, EmailStr, ConfigDict
from app.security.roles import UserRole

class Usuario(BaseModel):

    id: int
    nome: str = Field(min_length=3, max_length=100)
    email: EmailStr
    usuario: str = Field(min_length=6, max_length=50)
    senha: str

class UsuarioCreate(BaseModel):
    
    nome: str = Field(min_length=3, max_length=100)
    email: EmailStr
    usuario: str = Field(min_length=3, max_length=10)
    senha: str = Field(min_length=6, max_length=50)

    model_config = ConfigDict(from_attributes=True)

class UsuarioUpdate(BaseModel):

    id: int
    nome: str = Field(min_length=3, max_length=100)
    email: EmailStr
    usuario: str = Field(min_length=6, max_length=50)

    model_config = ConfigDict(from_attributes=True)

class UsuarioResponse(BaseModel):

    id: int
    nome: str = Field(min_length=3, max_length=100)
    email: EmailStr
    usuario: str
    perfil: UserRole

    model_config = ConfigDict(from_attributes=True)




