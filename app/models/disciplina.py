from app.database.config import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, CheckConstraint

class Disciplina(Base):

    __tablename__ = 'disciplinas'

    __table_args__ = (
        CheckConstraint(
            'carga_horaria > 0',
            name='ck_disciplinas_carga_horaria'
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
        )
    
    descricao: Mapped[str] = mapped_column(
        String(150), 
        nullable=False
        )
    
    carga_horaria: Mapped[int] = mapped_column(
        nullable=False
        )