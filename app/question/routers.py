from fastapi import APIRouter, Depends, HTTPException, Form, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.connection import get_db

from app.question.crud import get_all_questions, create_question, get_question, delete_question, get_question_answers
from app.question.shemas import QuestionOut, QuestionAnswersOut
import logging


router = APIRouter()
logger = logging.getLogger("app")


@router.post("/", response_model=QuestionOut)
async def create_user_endpoint(text: str, db: AsyncSession = Depends(get_db)):
    question = await create_question(db, text)
    logger.info(f"Создан новый вопрос {question.id}")
    return question


@router.get("/", response_model=list[QuestionOut])
async def get_all_questions_endpoint(db: AsyncSession = Depends(get_db)):
    questions = await get_all_questions(db)
    if not questions:
        raise HTTPException(status_code=404, detail="Вопросов нет")

    logger.info(f"Запрошены все вопросы")

    return questions


@router.get("/{id}", response_model=QuestionAnswersOut)
async def get_question_endpoint(question_id: int, db: AsyncSession = Depends(get_db)):

    question = await get_question_answers(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Вопроса нет")
    return question


@router.delete("/{id}", response_model=QuestionOut)
async def delete_question_endpoint(question_id: int, db: AsyncSession = Depends(get_db)):
    question = await get_question(db, question_id)

    if not question:
        raise HTTPException(status_code=404, detail="Вопроса нет")

    await delete_question(db, question=question)
    return question
