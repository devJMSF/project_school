from app.database.config import Base, engine
from app.routers.aluno import router_alunos
from app.routers.disciplina import router_disciplina
from app.routers.professor import router_professor
from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title="Escola API",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(router_alunos)
app.include_router(router_disciplina)
app.include_router(router_professor)

@app.get("/")
def home():
    return {"msg": "API da escola funcionando"}