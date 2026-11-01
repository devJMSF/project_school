import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.database.config import DbSession
from app.security.jwt import decodificar_access_token
from app.repositories import usuario as repo

bearer_scheme = HTTPBearer(
    auto_error=False
)

def get_current_user(
        credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
        db: DbSession = None
        ):

    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="token não informado",
            headers={"WWW-Authenticate": "Bearer"}
        )

    try:
        payload = decodificar_access_token(credentials.credentials)

        usuario_id = payload.get("sub")

        if not usuario_id:
            raise ValueError("identificador ausente")

        usuario_id = int(usuario_id)

    except (jwt.InvalidTokenError, ValueError, TypeError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="token invalido ou expirado",
            headers={"WWW-Authenticate": "Bearer"}
        )

    usuario = repo.buscar_por_id(
        db, usuario_id
    )

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="usuario nao encontrado",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return usuario


usuario_atual = Depends(get_current_user)