from typing import List

from sqlalchemy import Row, RowMapping
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload
from sqlalchemy.future import select
from app.answer.model import Answer


async def create_answer(db: AsyncSession, question_id, text: str) -> Answer:
    answer = Answer(question_id=question_id, text=text)
    db.add(answer)
    await db.commit()
    await db.refresh(answer)
    return answer


async def delete_answer(db: AsyncSession, answer: Answer) -> Answer:
    await db.delete(answer)
    await db.commit()
    return answer


async def get_answer(db: AsyncSession, answer_id: int) -> Answer:
    result = await db.execute(select(Answer).filter(Answer.id == answer_id))
    return result.scalars().first()




