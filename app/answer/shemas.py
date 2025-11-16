from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class AnswerCreate(BaseModel):
    text: str


class AnswerOut(AnswerCreate):
    id: int
    created_at: datetime
    user_id: UUID
    question_id: int

    class Config:
        from_attributes = True
