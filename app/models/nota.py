from app.database.config import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Date, CheckConstraint
from datetime import date

class Nota(Base):

    __tablename__ = 'notas'

    __table_args__ = (
        CheckConstraint(
            'valor >= 0 AND valor <= 10',
            name='ck_notas_valor'
        ),
        CheckConstraint(
            "tipo_avaliacao IN ('prova', 'trabalho', 'atividade')",
            name='ck_notas_tipo_avaliacao'
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    aluno_id: Mapped[int] = mapped_column(
        ForeignKey('alunos.id'),
        nullable=False
        )
    
    disciplina_id: Mapped[int] = mapped_column(
        ForeignKey('disciplinas.id'),
        nullable=False
        )
    
    professor_id: Mapped[int] = mapped_column(
        ForeignKey('professores.id'),
        nullable=False
        )

    valor: Mapped[float] = mapped_column(
        nullable=False
        )
    
    tipo_avaliacao: Mapped[str] = mapped_column(
        String(20), 
        nullable=False
        )
    
    data_avaliacao: Mapped[date] = mapped_column(
        Date, 
        nullable=False
    )