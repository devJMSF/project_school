from pydantic import BaseModel, Field
from typing import Optional, Literal

class Turma(BaseModel):

    id: int
    nome: str = Field(min_length=3, max_length=100)
    ano_letivo: int = Field(gt=2026)
    turno: Literal['manhã', 'tarde', 'noite']
    capacidade: int = Field(gt=0)

class TurmaCreate(BaseModel):
    
    nome: str = Field(min_length=3, max_length=100)
    ano_letivo: int = Field(gt=2026)
    turno: Literal['manhã', 'tarde', 'noite']
    capacidade: int = Field(gt=0)

class TurmaUpdate(BaseModel):

    id: int
    nome: str = Field(min_length=3, max_length=100)
    ano_letivo: int = Field(gt=2026)
    turno: Literal['manhã', 'tarde', 'noite']
    capacidade: int = Field(gt=0)

class TurmaResponse(BaseModel):

    id: int
    nome: str = Field(min_length=3, max_length=100)
    ano_letivo: int = Field(gt=2026)
    turno: Literal['manhã', 'tarde', 'noite']
    capacidade: int = Field(gt=0)
