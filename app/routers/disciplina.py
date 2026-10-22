from app.database.config import SessionLocal
from app.schemas.disciplina import DisciplinaCreate, DisciplinaUpdate, DisciplinaResponse
from app.services import disciplina as service
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router_disciplina = APIRouter(
    prefix="/disciplinas",
    tags=["Disciplinas"]
)

def obter_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

DbSession = Annotated[Session, Depends(obter_db)]

@router_disciplina.get("/", response_model=list[DisciplinaResponse])
def listar(db: DbSession):
    return service.listar_disciplinas(db)

@router_disciplina.post("/", response_model=DisciplinaResponse)
def criar(dados: DisciplinaCreate, db: DbSession):
    return service.criar_disciplina(db, dados)

@router_disciplina.delete("/{disciplina_id}", status_code=204)
def excluir(disciplina_id, db:DbSession):
    disciplina = service.exclui_disciplina(db, disciplina_id)

    if not disciplina:
        raise HTTPException(
            status_code=404,
            detail="disciplina não encontrada"
        )

@router_disciplina.patch("/", response_model=DisciplinaResponse)
def atualizar(dados: DisciplinaUpdate, db: DbSession):
    disciplina = service.atualizar_disciplina(db, dados)

    if not disciplina:
        raise HTTPException(
            status_code=404,
            detail="Disciplina não encontrada"            
        )

    return disciplina

@router_disciplina.get("/{disciplina_id}", response_model=DisciplinaResponse)
def buscar(disciplina_id: int, db: DbSession):
    disciplina = service.buscar_disciplina(db, disciplina_id)

    if not disciplina:
        raise HTTPException(
            status_code=404,
            detail="Disciplina não encontrada"
        )

    return disciplina