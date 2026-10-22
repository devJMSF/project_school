from app.models.disciplina import Disciplina
from sqlalchemy import select
from sqlalchemy.orm import Session

def listar(db: Session):
    return db.scalars(select(Disciplina)).all()

def buscar_por_id(db: Session, disciplina_id: int):
    return db.get(Disciplina, disciplina_id)

def criar(db: Session, dados: dict):
    disciplina = Disciplina(**dados)

    db.add(disciplina)
    db.commit()
    db.refresh(disciplina)

    return disciplina

def excluir(db: Session, disciplina: Disciplina):
    db.delete(disciplina)
    db.commit()
    