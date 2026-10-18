from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column
from app.database.config import Base
from datetime import date

class Aluno(Base):

    __tablename__ = 'alunos'

    id: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(
        String(100), 
        nullable=False
        )
    
    cpf: Mapped[str] = mapped_column(
        String(14), 
        unique=True, 
        nullable=False
        )
    
    data_nascimento: Mapped[date] = mapped_column(
        Date, 
        nullable=False
        )
    
    email: Mapped[str] = mapped_column(
        String(150), 
        unique=True, 
        nullable=False
        )
    
    celular: Mapped[str] = mapped_column(
        String(11), 
        unique=True,
        nullable=False
        ) 
    
    data_cadastro: Mapped[date] = mapped_column(
        Date,
        nullable=False
        )