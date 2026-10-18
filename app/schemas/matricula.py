from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import date

class Matricula(BaseModel):
    
    id: int[Optional]
    aluno_id: int
    turma_id: int
    data_matricula: date
    status: Literal['ativa', 'trancada', 'cancelada', 'concluída']