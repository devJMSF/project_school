from pydantic import BaseModel, Field, ConfigDict
from typing import Literal
from datetime import date

class Nota(BaseModel):

    id: int
    aluno_id: int
    disciplina_id: int
    professor_id: int

    valor: float = Field(ge=0, le=10)
    
    tipo_avaliacao: Literal['prova', 'trabalho', 'atividade']
    data_avaliacao: date

class NotaCreate(BaseModel):

    aluno_id: int
    disciplina_id: int
    professor_id: int

    valor: float = Field(ge=0, le=10)
    
    tipo_avaliacao: Literal['prova', 'trabalho', 'atividade']
    data_avaliacao: date

    model_config = ConfigDict(from_attributes=True)


class NotaUpdate(BaseModel):

    id: int
    aluno_id: int
    disciplina_id: int
    professor_id: int

    valor: float = Field(ge=0, le=10)
    
    tipo_avaliacao: Literal['prova', 'trabalho', 'atividade']
    data_avaliacao: date

    model_config = ConfigDict(from_attributes=True)


class NotaResponse(BaseModel):

    id: int
    aluno_id: int
    disciplina_id: int
    professor_id: int

    valor: float = Field(ge=0, le=10)
    
    tipo_avaliacao: Literal['prova', 'trabalho', 'atividade']
    data_avaliacao: date

    model_config = ConfigDict(from_attributes=True)