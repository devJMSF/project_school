from app.schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from app.database.config import DbSession
from app.services import usuario as service
from fastapi import APIRouter, HTTPException

router_usuario = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router_usuario.get("/", response_model=list[UsuarioResponse])
def listar(db: DbSession):
    return service.listar_usuarios(db)

@router_usuario.get("/{usuario_id}", response_model=UsuarioResponse)
def buscar(usuario_id: int, db: DbSession):
    return service.buscar_usuario(db, usuario_id)

@router_usuario.post("/", response_model=UsuarioResponse)
def criar(dados: UsuarioCreate, db: DbSession):
    return service.criar_usuario(db, dados)

@router_usuario.patch("/{usuario_id}", response_model=UsuarioResponse)
def atualizar(dados: UsuarioUpdate, db: DbSession):
    usuario = service.atualizar_usuario(db, dados)

    if not usuario: 
        raise HTTPException(
            status_code=404,
            detail="usuario não encontrado"
        )

    return usuario

@router_usuario.delete("/{usuario_id}", response_model=UsuarioResponse)
def excluir(usuario_id: int, db: DbSession):
    usuario = service.excluir_usuario(db, usuario_id)

    if not usuario: 
            raise HTTPException(
                status_code=404,
                detail="usuario não encontrado"
            )
    
    return usuario