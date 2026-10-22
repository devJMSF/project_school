from app.schemas.disciplina import DisciplinaCreate, DisciplinaUpdate
from app.repositories import disciplina as repo
from sqlalchemy.orm import Session

def listar_disciplinas(db: Session):
    return repo.listar(db)

def buscar_disciplina(db: Session, disciplina_id: int):
    return repo.buscar_por_id(db, disciplina_id)

def criar_disciplina(db: Session, dados: DisciplinaCreate):
    return repo.criar(db, dados.model_dump())

def atualizar_disciplina(db: Session, dados: DisciplinaUpdate):
    disciplina = repo.buscar_por_id(db, dados.id)

    if not disciplina:
        return None

    alteracoes = dados.model_dump(
        exclude_unset=True, 
        exclude={"id"},
    )

    for campo, valor in alteracoes.items():
        setattr(disciplina, campo, valor)

    db.commit()
    db.refresh(disciplina)

    return disciplina

def exclui_disciplina(db: Session, disciplina_id: int):
    disciplina = repo.buscar_por_id(db, disciplina_id)

    if not disciplina:
        return False

    repo.excluir(db, disciplina)

    return True
