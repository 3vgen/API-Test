from pydantic import BaseModel
from datetime import datetime
from app.answer.shemas import AnswerOut
from typing import List


class QuestionCreate(BaseModel):
    text: str


class QuestionOut(QuestionCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class QuestionAnswersOut(QuestionOut):
    answers: List[AnswerOut] = []