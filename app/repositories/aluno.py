from app.models.aluno import Aluno
from sqlalchemy import select
from sqlalchemy.orm import Session

def listar(db: Session):
    return db.scalars(select(Aluno)).all()

def buscar_por_id(db: Session, aluno_id: int):
    return db.get(Aluno, aluno_id)

def criar(db: Session, dados: dict):
    aluno = Aluno(**dados)

    db.add(aluno)
    db.commit()
    db.refresh(aluno)

    return aluno

def excluir(db: Session, aluno: Aluno):
    db.delete(aluno)
    db.commit()