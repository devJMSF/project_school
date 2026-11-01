from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repositories import usuario as repo
from app.security.hashing import verificar_senha
from app.security.jwt import criar_access_token

def autenticar_usuario(db: Session, email: str, senha: str):
    usuario = repo.buscar_por_email(db, email)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="email ou senha incorreto"
        )

    senha_valida = verificar_senha(senha, usuario.senha)

    if not senha_valida:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="email ou senha incorreto"
        )

    token = criar_access_token({
        "sub": str(usuario.id)
    })

    return token