from pydantic import BaseModel, EmailStr, Field
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