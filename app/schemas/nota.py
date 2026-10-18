from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import date

class Nota(BaseModel):

    id: int[Optional]
    aluno_id: int
    disciplina_id: int
    professor_id: int

    valor: float = Field(ge=0, le=10)
    
    tipo_avaliacao: Literal['prova', 'trabalho', 'atividade']
    data_avaliacao: date