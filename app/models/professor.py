from app.database.config import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date
from datetime import date

class Professor(Base):

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
    
    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False
        )
    
    especialidade: Mapped[str] = mapped_column(
        String(100),
        nullable=False
        )
    
    data_contratacao: Mapped[date] = mapped_column(
        Date,
        nullable=False
        )
    
    ativo: Mapped[bool] = mapped_column(
        default=True,
        nullable=False
    )