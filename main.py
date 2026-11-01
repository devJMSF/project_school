from app.routers.aluno import router_alunos
from app.routers.disciplina import router_disciplina
from app.routers.professor import router_professor
from app.routers.turma import router_turma
from app.routers.nota import router_nota
from app.routers.usuario import router_usuario
from app.routers.autenticacao import router_autenticacao
from fastapi import FastAPI

app = FastAPI(
    title="Escola API",
    version="1.0.0"
)

app.include_router(router_alunos)
app.include_router(router_disciplina)
app.include_router(router_professor)
app.include_router(router_turma)
app.include_router(router_nota)
app.include_router(router_usuario)
app.include_router(router_autenticacao)

@app.get("/")
def home():
    return {"msg": "API da escola funcionando"}