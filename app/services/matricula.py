from app.schemas.matricula import MatriculaCreate, MatriculaUpdate
from app.repositories import matricula as repo
from sqlalchemy.orm import Session

def listar_matriculas(db: Session):
    return repo.listar(db)

def buscar_matricula(db: Session, matricula_id: int):
    return repo.buscar_por_id(db, matricula_id)

def criar_matricula(db: Session, dados: MatriculaCreate):
    return repo.criar(db, dados.model_dump())

def atualizar_matriculas(db: Session, dados: MatriculaUpdate):
    matriculas = repo.buscar_por_id(db, dados.id)

    if not matriculas:
        return None

    alterar = dados.model_dump(
        exclude_unset=True,
        exclude={"id"},
    )

    for campo, valor in alterar.items():
        setattr(matriculas, campo, valor)

    db.commit()
    db.refresh(matriculas)

    return matriculas

def excluir_matricula(db: Session, matricula_id: int):
    matricula = repo.buscar_por_id(db, matricula_id)

    if not matricula:
        return None

    repo.excluir(db, matricula)

    return True