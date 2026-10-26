from app.models.matricula import Matricula
from sqlalchemy.orm import Session
from sqlalchemy import select

def listar(db: Session):
    return db.scalars(select(Matricula)).all()

def buscar_por_id(db: Session, matricula_id: int):
    return db.get(Matricula, matricula_id)

def criar(db: Session, dados: dict):
    matricula = Matricula(**dados)

    db.add(matricula)
    db.commit()
    db.refresh(matricula)

    return matricula

def excluir(db: Session, matricula: Matricula):
    db.delete(matricula)
    db.commit()