from pydantic import BaseModel, Field
from typing import Optional, Literal

class Turma(BaseModel):

    id: int[Optional]
    nome: str = Field(min_length=3, max_length=100)
    ano_letivo: int = Field(gt=2026)
    turno: Literal['manhã', 'tarde', 'noite']
    capacidade: int = Field(gt=0)