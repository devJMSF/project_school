from app.repositories import professor as repo
from app.schemas.professor import ProfessorCreate, ProfessorUpload
from sqlalchemy.orm import Session

def listar_professores(db: Session):
    return repo.listar(db)

def buscar_professor(db: Session, professor_id: int):
    return repo.buscar_por_id(db, professor_id)

def buscar_professor_por_cpf(db: Session, professor_cpf: str):
    return repo.buscar_por_cpf(db, professor_cpf)

def criar_professor(db: Session, dados: ProfessorCreate):
    return repo.criar(db, dados.model_dump())

def atualizar_professor(db: Session, dados: ProfessorUpload):
    professor = repo.buscar_por_id(db, dados.id)

    if not professor:
        return None

    alteracoes = dados.model_dump(
        exclude_unset=True,
        exclude={"id"},
    )

    for campo, valor in alteracoes.items():
        setattr(professor, campo, valor)

    db.commit()
    db.refresh(professor)

    return professor


    

def excluir_professor(db: Session, professor_id: int):
    professor = repo.buscar_por_id(db, professor_id)

    if not professor:
        return None

    repo.excluir(db, professor) 

    return True
