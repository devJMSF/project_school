from app.models.turma import Turma
from sqlalchemy import select
from sqlalchemy.orm import Session

def listar(db: Session):
    return db.scalars(select(Turma)).all()

def buscar_por_id(db: Session, turma_id: int):
    return db.get(Turma, turma_id)

def criar(db: Session, dados: dict):
    turma = Turma(**dados)

    db.add(turma)
    db.commit()
    db.refresh(turma)

    return turma

def excluir(db: Session, turma: Turma):
    db.delete(turma)
    db.commit()
    