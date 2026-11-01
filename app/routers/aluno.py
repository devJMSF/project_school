from app.database.config import DbSession
from app.schemas.aluno import AlunoCreate, AlunoUpdate, AlunoResponse
from app.services import aluno as service
from fastapi import APIRouter, HTTPException, Depends
from app.security.dependencies import get_current_user

router_alunos = APIRouter(
    prefix="/alunos", 
    tags=["Alunos"],
    dependencies=[Depends(get_current_user)]
)

@router_alunos.get("/", response_model=list[AlunoResponse])
def listar(db: DbSession):
    return service.listar_alunos(db)

@router_alunos.get("/{aluno_id}", response_model=AlunoResponse)
def buscar(aluno_id: int, db: DbSession):
    aluno = service.buscar_aluno(db, aluno_id)

    if not aluno:
        raise HTTPException(
            status_code=404,
            detail="aluno não encontrado"
        )

    return aluno

@router_alunos.post("/", response_model=AlunoResponse)
def criar(dados: AlunoCreate, db: DbSession):
    return service.criar_aluno(db, dados)


@router_alunos.patch("/", response_model=AlunoResponse)
def atualizar(dados: AlunoUpdate, db: DbSession):
    aluno = service.atualizar_aluno(db, dados)

    if not aluno:
        raise HTTPException(
            status_code=404,
            detail="aluno não encontrado"
        )

    return aluno

@router_alunos.delete("/{aluno_id}", status_code=204)
def excluir(aluno_id: int, db: DbSession):
    aluno = service.exclui_aluno(db, aluno_id)

    if not aluno:
        raise HTTPException(
                    status_code=404,
                    detail="aluno não encontrado"
                )