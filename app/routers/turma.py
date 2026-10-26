from app.schemas.turma import TurmaResponse, TurmaCreate, TurmaUpdate
from typing import Annotated
from app.database.config import SessionLocal
from app.services import turma as service
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

router_turma = APIRouter(
    prefix="/turmas",
    tags=["Turmas"]
)

def obter_db():
    db = SessionLocal()

    try:
        yield db
    except:
        db.close()

DbSession = Annotated[Session, Depends(obter_db)]

@router_turma.get("/", response_model=list[TurmaResponse])
def listar(db: DbSession):
    return service.listar_turmas(db)

@router_turma.get("/{turma_id}",response_model=TurmaResponse)
def buscar(turma_id: int, db: DbSession):
    return service.buscar_turma(db, turma_id)

@router_turma.post("/", status_code=201)
def criar(dados: TurmaCreate, db: DbSession):
    return service.criar_turma(db, dados)

@router_turma.patch("/", response_model=TurmaResponse)
def listar(dados: TurmaUpdate, db: DbSession):
    return service.atualizar_turma(db, dados)

@router_turma.delete("/{turma_id}", status_code=204)
def excluir(turma_id: int, db: DbSession):
    return service.excluir_turma(db, turma_id)
