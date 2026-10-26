from sqlalchemy.orm import Session
from app.models.professor import Professor
from sqlalchemy import select

def listar(db: Session):
    return db.scalars(select(Professor))

def buscar_por_id(db: Session, processor_id):
    return db.get(Professor, processor_id)

def criar(db: Session, dados: dict):
    professor = Professor(**dados)

    db.add(professor)
    db.commit()
    db.refresh(professor)

    return professor

def excluir(db: Session, professor: Professor):
    db.delete(professor)
    db.commit()