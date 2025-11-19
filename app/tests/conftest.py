import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.connection import get_db


# Мок для бд
class FakeDB:
    def __init__(self):
        self.questions = []
        self.next_id = 1

    def create_question(self, text):
        question = {"id": self.next_id, "text": text}
        self.questions.append(question)
        self.next_id += 1
        return question


@pytest.fixture
def client():
    fake_db = FakeDB()

    # Подменяем зависимость БД
    app.dependency_overrides[get_db] = lambda: fake_db

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()
