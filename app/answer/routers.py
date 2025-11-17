from fastapi import APIRouter, Depends, HTTPException, Form, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.connection import get_db

from app.answer.crud import get_answer, create_answer, delete_answer, create_answer_by_old_user
from app.answer.shemas import AnswerCreate, AnswerOut
from uuid import UUID


router = APIRouter()


@router.post("/{question_id}", response_model=AnswerOut)
async def create_answer_endpoint(question_id: int, text: str, db: AsyncSession = Depends(get_db)):
    answer = await create_answer(db, question_id=question_id, text=text)
    return answer


@router.post("/{question_id}/ {user_id}", response_model=AnswerOut)
async def create_answer_endpoint(question_id: int, text: str, user_id: UUID, db: AsyncSession = Depends(get_db)):
    answer = await create_answer_by_old_user(db, question_id=question_id, text=text, user_id=user_id)
    return answer


@router.get("/{id}", response_model=AnswerOut)
async def get_answer_endpoint(answer_id: int, db: AsyncSession = Depends(get_db)):

    answer = await get_answer(db, answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Вопроса нет")
    return answer


@router.delete("/{id}", response_model=AnswerOut)
async def delete_answer_endpoint(answer_id: int, db: AsyncSession = Depends(get_db)):
    answer = await get_answer(db, answer_id)

    if not answer:
        raise HTTPException(status_code=404, detail="Вопроса нет")

    await delete_answer(db, answer=answer)
    return answer
