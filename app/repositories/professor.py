from sqlalchemy.orm import Session
from app.models.professor import Professor
from sqlalchemy import select

def listar(db: Session):
    return db.scalars(select(Professor))

def buscar_por_id(db: Session, professor_id):
    return db.get(Professor, professor_id)

def buscar_por_cpf(db: Session, professor_cpf):
    professor = select(Professor).where(Professor.cpf == professor_cpf)
    return db.scalar(professor)

def criar(db: Session, dados: dict):
    professor = Professor(**dados)

    db.add(professor)
    db.commit()
    db.refresh(professor)

    return professor

def excluir(db: Session, professor: Professor):
    db.delete(professor)
    db.commit()