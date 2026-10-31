from app.models.nota import Nota
from sqlalchemy.orm import Session
from sqlalchemy import select

def listar(db: Session) -> list[Nota]:
    return db.scalars(select(Nota))

def buscar_por_id(db: Session, nota_id: int):
    return db.get(Nota, nota_id)

def criar(db: Session, dados: dict) -> None:
    nota = Nota(**dados)

    db.add(nota)
    db.commit()
    db.refresh(nota)

    return nota

def excluir(db: Session, nota: Nota) -> None:
    db.delete(nota)
    db.commit()
