from app.schemas.turma import TurmaCreate, TurmaUpdate
from app.repositories import turma as repo
from sqlalchemy.orm import Session

def listar_turmas(db: Session):
    return repo.listar(db)

def buscar_turma(db: Session, turma_id: int):
    return repo.buscar_por_id(db, turma_id)

def criar_turma(db: Session, dados: TurmaCreate):
    return repo.criar(db, dados.model_dump())

def excluir_turma(db: Session, turma_id: int):
    turma = repo.buscar_por_id(db, turma_id)

    if not turma:
        return None

    repo.excluir(db, turma)

    return True

def atualizar_turma(db: Session, dados: TurmaUpdate):
    turma = repo.buscar_por_id(db, dados.id)

    if not turma:
        return None

    alteracao = dados.model_dump(
        exclude_unset=True,
        exclude={"id"},
    )

    for campo, valor in alteracao.items():
        setattr(turma, campo, valor)

    db.commit()
    db.refresh(turma)

    return turma


