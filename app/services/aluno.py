from app.schemas.aluno import AlunoCreate, AlunoUpdate
from app.repositories import aluno as repo
from sqlalchemy.orm import Session

def listar_alunos(db: Session):
    return repo.listar(db)

def buscar_aluno(db: Session, aluno_id: int):
    return repo.buscar_por_id(db, aluno_id)

def criar_aluno(db: Session, dados: AlunoCreate):
    return repo.criar(
        db, 
        dados.model_dump(exclude={"data_nascimento"}) |
        {"data_nascimento": dados.data_nascimento}
    )

def atualizar_aluno(db: Session, dados: AlunoUpdate):
    aluno = repo.buscar_por_id(db, dados.id)

    if not aluno:
        return None

    alteracoes = dados.model_dump(
        exclude_unset=True,
        exclude={"id"}, 
    )

    for campo, valor in alteracoes.items():
        setattr(aluno, campo, valor)

    db.commit()
    db.refresh(aluno)

    return aluno

def exclui_aluno(db: Session, aluno_id: int):
    aluno = repo.buscar_por_id(db, aluno_id)

    if not aluno:
        return None

    repo.excluir(db, aluno)

    return True
