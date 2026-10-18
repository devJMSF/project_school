from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import date

class Aluno(BaseModel):

    id: int[Optional]
    nome: str = Field(min_length=3, max_length=100)
    cpf: str = Field(min_length=11, max_length=11)
    data_nascimento: date
    email: EmailStr
    telefone: str
    data_cadastro: date

class AlunoCreate(BaseModel):

    nome: str = Field(min_length=3, max_length=100)
    cpf: str = Field(min_length=11, max_length=11)
    data_nascimento: date
    email: EmailStr
    telefone: str

    model_config = ConfigDict(from_attributes=True)

class AlunoUpdate(BaseModel):

    id: int
    nome: str | None = Field(default=None, min_length=3, max_length=100)
    cpf: str | None = Field(default=None, min_length=11, max_length=11)
    data_nascimento: date | None = None
    email: EmailStr | None = None
    telefone: str | None = None

    model_config = ConfigDict(from_attributes=True)

class AlunoResponse(BaseModel):

    id: int
    nome: str
    cpf: str
    data_nascimento: date | None
    email: EmailStr | None
    telefone: str | None

    model_config = ConfigDict(from_attributes=True)