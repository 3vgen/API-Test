# Q&A FastAPI Project

Асинхронное приложение на FastAPI с PostgreSQL и миграциями Alembic.

## Требования

- Docker 20+  
- Docker Compose 1.29+  

*(Все зависимости устанавливаются внутри Docker, Python локально не нужен)*

---

## Структура проекта
Структура проекта
.
├── alembic.ini
├── app
│   ├── __init__.py
│   ├── answer
│   │   ├── __init__.py
│   │   ├── crud.py
│   │   ├── model.py
│   │   ├── routers.py
│   │   └── shemas.py
│   ├── app.log
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── migrations
│   ├── db
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── connection.py
│   ├── logging_config.py
│   ├── main.py
│   ├── question
│   │   ├── __init__.py
│   │   ├── crud.py
│   │   ├── model.py
│   │   ├── routers.py
│   │   └── shemas.py
│   └── tests
│       ├── __init__.py
│       ├── conftest.py
│       └── test_question.py
├── app.log
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt

---

## Быстрый старт (Docker)

1. Клонирование репозитория:
```bash
git clone <REPO_URL>
cd <REPO_FOLDER>
```

2. Создать в корне .env файл
```
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/qna
```

3. Сборка Docker образов:
``` bash
docker compose build
```

3. Запуск контейнеров
``` bash
docker compose up -d
```

4. Применение миграций
``` bash
docker compose exec web alembic upgrade head
```

5. Открыть Swagger для проверки API: http://localhost:8000/docs
