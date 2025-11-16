import uvicorn
from fastapi import FastAPI
from app.db.connection import engine
from app.db.base import Base
from app.question.routers import router as question_router
from app.answer.routers import router as answer_router
from contextlib import asynccontextmanager
from app.question.model import Question
from app.answer.model import Answer


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    # Сюда потом добавлю подключение redis, и мб очередь сообщений
    print("Приложение запускается.")
    yield
    # Shutdown
    await engine.dispose()
    print("Приложение остановлено, соединение с БД закрыто.")


app = FastAPI(title="test", lifespan=lifespan)

app.include_router(question_router, prefix="/questions", tags=["API"])
app.include_router(answer_router, prefix="/answer", tags=["API"])
if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=80,
        reload=True
    )
