from app.database.config import Base, engine
from app.models.aluno import Aluno
from app.routers.aluno import router as aluno_router
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

app.include_router(aluno_router)

@app.get("/")
def home():
    return {"msg": "API da escola funcionando"}