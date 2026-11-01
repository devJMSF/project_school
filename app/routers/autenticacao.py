from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.autenticacao import LoginRequest, TokenResponse
from app.database.config import DbSession
from app.services.autenticacao import autenticar_usuario

router_autenticacao = APIRouter(
    prefix="/auth",
    tags=["Autenticação"]
)

@router_autenticacao.post("/login", response_model=TokenResponse)
def login(dados: LoginRequest, db: DbSession):
    token = autenticar_usuario(db, dados.email, dados.senha)

    return {
        "access_token": token, 
        "token_type": "bearer"
    }