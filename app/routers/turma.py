from app.schemas.turma import TurmaResponse, TurmaCreate, TurmaUpdate
from app.database.config import DbSession
from app.services import turma as service
from fastapi import HTTPException, APIRouter
from sqlalchemy.orm import Session

router_turma = APIRouter(
    prefix="/turmas",
    tags=["Turmas"]
)

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
def Atualizar(dados: TurmaUpdate, db: DbSession):
    turma = service.atualizar_turma(db, dados)

    if not turma:
        raise HTTPException(
            status_code=404,
            detail="turma não encontrada"
        )
    
    return turma

@router_turma.delete("/{turma_id}", status_code=204)
def excluir(turma_id: int, db: DbSession):
    turma = service.excluir_turma(db, turma_id)
    
    if not turma:
        raise HTTPException(
            status_code=404,
            detail="turma não encontrada"
        )
    
    return turma
