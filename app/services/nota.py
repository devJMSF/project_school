from sqlalchemy.orm import Session
from app.schemas.nota import NotaCreate, NotaUpdate
from app.repositories import nota as repo
from app.models.nota import Nota

def listar_notas(db: Session):
    return repo.listar(db)

def buscar_nota(db: Session, nota_id):
    return repo.buscar_por_id(db, nota_id)

def criar_nota(db: Session, dados: NotaCreate):
    return repo.criar(db, dados.model_dump())

def atualizar_nota(db: Session, dados: NotaUpdate):
    nota = repo.buscar_por_id(db, dados.id)

    if not nota:
        return None

    alteracoes = dados.model_dump(
        exclude_unset=True,
        exclude={"id"},
    )

    for campo, valor in alteracoes.items():
        setattr(nota, campo, valor)

    db.commit()
    db.refresh(nota)

    return nota

def excluir_nota(db: Session, nota_id: int):
    nota = repo.buscar_por_id(db, nota_id)

    if not nota:
        return False

    db.delete(nota)
    db.commit()

    return True





