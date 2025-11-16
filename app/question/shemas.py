from pydantic import BaseModel
from datetime import datetime


class QuestionCreate(BaseModel):
    text: str


class QuestionOut(QuestionCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
