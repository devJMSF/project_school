from pydantic import BaseModel
from datetime import date

class Matricula(BaseModel):
    
    id: int

    aluno_id: int    
    turma_id: int    
    data_matricula: date    
    status: str | None

class MatriculaCreate(BaseModel):
    
    aluno_id: int    
    turma_id: int    
    data_matricula: date    
    status: str | None

class MatriculaUpdate(BaseModel):
    
    id: int    
    aluno_id: int    
    turma_id: int    
    data_matricula: date    
    status: str | None

class MatriculaResponse(BaseModel):
    
    id: int
    
    aluno_id: int    
    turma_id: int    
    data_matricula: date    
    status: str | None