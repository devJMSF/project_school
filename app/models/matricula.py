from app.database.config import Base
from sqlalchemy import String, Date, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

class Matricula(Base):

    __tablename__ = 'matriculas'

    __table_args__ = (
        CheckConstraint(
            "status IN ('ativa', 'trancada', 'cancelada', 'concluída')",
            name='ck_matriculas_status'
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    aluno_id: Mapped[int] = mapped_column(
        ForeignKey('alunos.id'),
        nullable=False)
    
    turma_id: Mapped[int] = mapped_column(
        ForeignKey('turmas.id'),
        nullable=False)
    
    data_matricula: Mapped[date] = mapped_column(
        Date, 
        nullable=False,
        default=date.today)
    
    status: Mapped[str] = mapped_column(
        String(20), 
        nullable=False,
        default='ativa'
    )