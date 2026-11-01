from app.schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse
from app.database.config import DbSession
from app.services import usuario as service
from fastapi import APIRouter, HTTPException, Depends
from app.security.dependencies import get_current_user

router_usuario = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router_usuario.get("/", response_model=list[UsuarioResponse])
def listar(db: DbSession, usuario_atual = Depends(get_current_user)):
    return service.listar_usuarios(db)    

@router_usuario.get("/{usuario_id}", response_model=UsuarioResponse)
def buscar(usuario_id: int, db: DbSession,  usuario_atual = Depends(get_current_user)):
    usuario = service.buscar_usuario(db, usuario_id)

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="aluno não encontrado"
        )

    return usuario

@router_usuario.post("/", response_model=UsuarioResponse)
def criar(dados: UsuarioCreate, db: DbSession):
    return service.criar_usuario(db, dados)

@router_usuario.patch("/", response_model=UsuarioResponse)
def atualizar(dados: UsuarioUpdate, db: DbSession,  usuario_atual = Depends(get_current_user)):
    usuario = service.atualizar_usuario(db, dados)

    if not usuario: 
        raise HTTPException(
            status_code=404,
            detail="usuario não encontrado"
        )

    return usuario

@router_usuario.delete("/{usuario_id}", status_code=204)
def excluir(usuario_id: int, db: DbSession,  usuario_atual = Depends(get_current_user)):
    usuario = service.excluir_usuario(db, usuario_id)

    if not usuario: 
            raise HTTPException(
                status_code=404,
                detail="usuario não encontrado"
            )
    
    return usuario