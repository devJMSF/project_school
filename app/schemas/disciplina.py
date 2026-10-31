from pydantic import BaseModel, Field, ConfigDict

class Disciplina(BaseModel):

    id: int
    nome: str = Field(min_length=3, max_length=100)
    descricao: str = Field(min_length=3, max_length=100)
    carga_horaria: int = Field(gt=0)


class DisciplinaCreate(BaseModel):
    
    nome: str = Field(min_length=3, max_length=100)
    descricao: str = Field(min_length=3, max_length=100)
    carga_horaria: int = Field(gt=0)

    model_config = ConfigDict(from_attributes=True)

class DisciplinaUpdate(BaseModel):

    id: int
    nome: str = Field(default=None, min_length=3, max_length=100)
    descricao: str = Field(default=None, min_length=3, max_length=100)
    carga_horaria: int = Field(default=None, gt=0)

    model_config = ConfigDict(from_attributes=True)

class DisciplinaResponse(BaseModel):

    id: int
    nome: str 
    descricao: str 
    carga_horaria: int 

    model_config = ConfigDict(from_attributes=True)