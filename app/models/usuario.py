from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum as SQLAchemyEnum
from app.database.config import Base
from app.security.roles import UserRole

class Usuario(Base):

    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    
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
        nullable=False
        )

    perfil: Mapped[UserRole] = mapped_column(
        SQLAchemyEnum(UserRole),
        nullable=False,
        default=UserRole.USER
        )

