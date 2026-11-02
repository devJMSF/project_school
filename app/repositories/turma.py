from app.models.turma import Turma
from app.models.matricula import Matricula
from app.models.aluno import Aluno
from sqlalchemy import select
from sqlalchemy.orm import Session

def listar(db: Session):
    return db.scalars(select(Turma)).all()

def buscar_por_id(db: Session, turma_id: int):
    return db.get(Turma, turma_id)

def listar_alunos_por_turma(db: Session, turma_id: int):
    query = (
        select(Aluno)
        .join(Matricula, Matricula.aluno_id == Aluno.id)
        .where(Matricula.turma_id == turma_id)
        .distinct()
    )

    return db.scalars(query).all()

def criar(db: Session, dados: dict):
    turma = Turma(**dados)

    db.add(turma)
    db.commit()
    db.refresh(turma)

    return turma

def excluir(db: Session, turma: Turma):
    db.delete(turma)
    db.commit()
    