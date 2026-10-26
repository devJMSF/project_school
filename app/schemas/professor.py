from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import date

class Professor(BaseModel):

    id: Optional[int]
    nome: str = Field(min_length=3, max_length=100)
    cpf: str = Field(min_length=11, max_length=11)
    email: EmailStr
    especialidade: str = Field(min_length=3, max_length=100)
    data_contratacao: date
    ativo: bool = True


class ProfessorCreate(BaseModel):

    nome: str = Field(min_length=3, max_length=100)
    cpf: str = Field(min_length=11, max_length=11)
    email: EmailStr
    especialidade: str = Field(min_length=3, max_length=100)
    data_contratacao: date
    ativo: bool = True


class ProfessorUpload(BaseModel):

    id: int
    nome: str = Field(min_length=3, max_length=100)
    cpf: str = Field(min_length=11, max_length=11)
    email: EmailStr
    especialidade: str = Field(min_length=3, max_length=100)
    data_contratacao: date
    ativo: bool = True

class ProfessorResponse(BaseModel):

    id: int
    nome: str = Field(min_length=3, max_length=100)
    cpf: str = Field(min_length=11, max_length=11)
    email: EmailStr
    especialidade: str = Field(min_length=3, max_length=100)
    data_contratacao: date
    ativo: bool = True