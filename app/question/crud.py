from typing import List

from sqlalchemy import Row, RowMapping
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.future import select
from app.question.model import Question


async def create_question(db: AsyncSession, text: str) -> Question:
    question = Question(text=text)
    db.add(question)
    await db.commit()
    await db.refresh(question)
    return question


async def delete_question(db: AsyncSession, question: Question) -> Question:
    await db.delete(question)
    await db.commit()
    return question


async def get_question(db: AsyncSession, question_id: int) -> Question:
    result = await db.execute(select(Question).filter(Question.id == question_id))
    return result.scalars().first()


async def get_all_questions(db: AsyncSession) -> List[Question]:
    result = await db.execute(select(Question))
    return result.scalars().all()
