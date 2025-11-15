import uvicorn
from fastapi import FastAPI
from app.db.connection import engine
from app.db.base import Base

from contextlib import asynccontextmanager


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


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=80,
        reload=True
    )