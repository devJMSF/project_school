from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import date

class Professor(BaseModel):

    id: int[Optional]
    nome: str = Field(min_length=3, max_length=100)
    cpf: str = Field(min_length=11, max_length=11)
    email: EmailStr
    especialidade: str = Field(min_length=11, max_length=11)
    data_contratacao: date
    ativo: bool