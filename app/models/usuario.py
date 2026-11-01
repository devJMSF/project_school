from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.database.config import Base

class Usuario(Base):

    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    
    nome: Mapped[str] = mapped_column(
        String(100), 
        nullable=False
        )
    
    email: Mapped[str] = mapped_column(
        unique=True,
        nullable=False
        )
    
    usuario: Mapped[str]= mapped_column(
        String(100), 
        nullable=False
        )
    
    senha: Mapped[str] = mapped_column(
        unique=True, 
        nullable=False
        )

