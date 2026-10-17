from pydantic import BaseModel, Field
from typing import Optional

class Diciplina(BaseModel):

    id: int[Optional]
    nome: str = Field(min_length=3, max_length=100)
    descricao: str = Field(min_length=3, max_length=100)
    carga_horaria: int = Field(gt=0)