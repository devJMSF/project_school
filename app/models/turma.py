from app.database.config import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, CheckConstraint

class Turma(Base):

    __tablename__ = 'turmas'

    __table_args__ = (
    
    CheckConstraint('ano_letivo >= 2025',
                    name='ck_turmas_ano_letivo'),
    
    CheckConstraint('capacidade > 0',
                    name='ck_turmas_capacidade'
        ),
    CheckConstraint("turno IN ('manhã', 'tarde', 'noite')",
                    name='ck_turmas_turno')
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(
        String(100), 
        nullable=False
        )
    
    ano_letivo: Mapped[int] = mapped_column(
        nullable=False
        )
    
    turno: Mapped[str] = mapped_column(
        String(10),
        nullable=False
    )

    capacidade: Mapped[int] = mapped_column(
        nullable=False
    )