from app.database.config import DbSession
from app.services import matricula as service
from app.schemas.matricula import MatriculaResponse, MatriculaUpdate, MatriculaCreate
from app.security.dependencies import get_current_user
from fastapi import APIRouter, Depends, HTTPException

router_matricula = APIRouter(
    prefix="/matriculas",
    tags=["Matriculas"], 
    dependencies=[Depends(get_current_user)]
)

@router_matricula.get("/", response_model=list[MatriculaResponse])
def listar(db: DbSession):
    return service.listar_matriculas(db)

@router_matricula.get("/{matricula_id}", response_model=MatriculaResponse)
def buscar(matricula_id: int, db: DbSession):
    matricula = service.buscar_matricula(db, matricula_id)

    if not matricula:
        raise HTTPException(
            status_code=404,
            detail="matricula não encontrada"
        )
    return matricula

@router_matricula.post("/", response_model=MatriculaResponse)
def criar(dados: MatriculaCreate, db: DbSession):
    matricula = service.criar_matricula(db, dados)

    if not matricula:
            raise HTTPException(
                status_code=404,
                detail="matricula não encontrada"
            )
    
    return matricula

@router_matricula.patch("/{matricula_id}", response_model=MatriculaResponse)
def atualizar(dados: MatriculaUpdate, db: DbSession):
    matricula = service.atualizar_matriculas(db, dados)

    if not matricula:
                raise HTTPException(
                    status_code=404,
                    detail="matricula não encontrada"
                )
        
    return matricula

@router_matricula.delete("/{matricula_id}", status_code=204)
def excluir(matricula_id: int, db: DbSession):
    matricula = service.excluir_matricula(db, matricula_id)

    if not matricula:
                raise HTTPException(
                    status_code=404,
                    detail="matricula não encontrada"
                )
        
    return matricula