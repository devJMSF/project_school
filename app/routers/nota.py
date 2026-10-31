from app.database.config import DbSession
from app.schemas.nota import NotaCreate, NotaUpdate, NotaResponse
from app.services import nota as service
from typing import Annotated
from fastapi import APIRouter, HTTPException

router_nota = APIRouter(
    prefix="/notas",
    tags=["Notas"]
)

@router_nota.get("/", response_model=list[NotaResponse])
def listar(db: DbSession):
    return service.listar_notas(db)

@router_nota.get("/{nota_id}", response_model=NotaResponse)
def buscar(nota_id: int, db: DbSession):
    return service.buscar_nota(db, nota_id)

@router_nota.post("/", status_code=201)
def criar(dados: NotaCreate, db: DbSession):
    return service.criar_nota(db, dados)

@router_nota.patch("/", response_model=NotaResponse)
def atualizar(nota: NotaUpdate, db: DbSession):
    nota = service.atualizar_nota(db, nota)

    if not nota:
        raise HTTPException(
            status_code=404,
            detail="nota nao encontrada"
        )

    return nota

@router_nota.delete("/{nota_id}", status_code=204)
def exclir(nota_id: int, db: DbSession):
    return service.excluir_nota(db, nota_id)
