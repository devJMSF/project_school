from app.models.usuario import Usuario
from sqlalchemy.orm import Session
from sqlalchemy import select

def listar(db: Session):
    return db.scalars(select(Usuario))

def buscar_por_id(db: Session, usuario_id: int):
    return db.get(Usuario, usuario_id)

def criar(db: Session, dados: dict):
    usuario = Usuario(**dados)

    print(usuario)

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario

def excluir(db: Session, usuario: Usuario):
    db.delete(usuario)
    db.commit()

