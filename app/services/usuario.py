from app.schemas.usuario import UsuarioCreate, UsuarioUpdate
from app.repositories import usuario as repo
from app.security.hashing import gerar_hash
from sqlalchemy.orm import Session

def listar_usuarios(db: Session):
    return repo.listar(db)

def buscar_usuario(db: Session, usuario_id):
    return repo.buscar_por_id(db, usuario_id)

def criar_usuario(db: Session, dados: UsuarioCreate):
    dados_usuario =  dados.model_dump()
    dados_usuario["senha"] = gerar_hash(dados_usuario["senha"])

    return repo.criar(db, dados_usuario)

def atualizar_usuario(db: Session, dados: UsuarioUpdate):
    usuario = repo.buscar_por_id(db, dados.id)

    if not usuario:
        return None

    alteracoes = dados.model_dump(
        exclude_unset=True,
        exclude={"id"},
    )

    for campo, valor in alteracoes.items():
        setattr(usuario, campo, valor)

    db.commit()
    db.refresh(usuario)

    return usuario

def excluir_usuario(db: Session, usuario_id: int):
    usuario = repo.buscar_por_id(db, usuario_id)

    if not usuario:
        return None

    repo.excluir(db, usuario)

    return True