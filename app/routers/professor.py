from app.schemas.professor import ProfessorCreate, ProfessorUpload, ProfessorResponse
from app.services import professor as service
from app.database.config import DbSession
from fastapi import APIRouter, HTTPException, Depends
from app.security.dependencies import get_current_user

router_professor = APIRouter(
    prefix="/professores",
    tags=["Professores"], 
    dependencies=[Depends(get_current_user)]
)

@router_professor.get("/", response_model=list[ProfessorResponse])
def listar(db: DbSession):
    return service.listar_professores(db)

@router_professor.post("/", status_code=201)
def criar(dados: ProfessorCreate, db: DbSession):
    return service.criar_professor(db, dados)

@router_professor.delete("/{professor_id}", status_code=204)
def excluir(professor_id: int, db: DbSession):
    professor = service.excluir_professor(db, professor_id)

    if not professor:
        raise HTTPException(
            status_code=404,
            detail="professor não encontrado"
        )

@router_professor.patch("/", response_model=ProfessorResponse)
def atualizar(dados: ProfessorUpload, db: DbSession):
    professor = service.atualizar_professor(db, dados)

    if not professor:
        raise HTTPException(
            status_code=404,
            detail="professor não encontrado"
            )

    return professor

@router_professor.get("/{professor_id}", response_model=ProfessorResponse)
def buscar(professor_id: int, db: DbSession):
    professor = service.buscar_professor(db, professor_id)

    if not professor:
        raise HTTPException(
            status_code=404, 
            detail="processor não encontrado"
        )
    
    return professor


