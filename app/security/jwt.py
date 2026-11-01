import jwt
from app.core.config import settings
from datetime import datetime, timedelta, timezone

def criar_access_token(dados: dict, expires_delta: timedelta | None = None) -> str:

    payload = dados.copy()

    agora = datetime.now(timezone.utc)

    expiracao = agora + timedelta(
        minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        )

    payload.update({
        "iat": agora,
        "exp": expiracao
    })

    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return token

def decodificar_access_token(token: str) -> dict:

    payload = jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM]
    )

    return payload