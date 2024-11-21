from fastapi import APIRouter
from schema import *
from fastapi import FastAPI, Depends
from database import UserRepository, QuizRepository, QuestionRepository


user_router = APIRouter(
    prefix="/users",
    tags=['users']
)

quiz_router = APIRouter(
    prefix='/quizes',
    tags=['quizes']
)

question_router = APIRouter(
    prefix='/questions',
    tags=['questions']
)


@user_router.post('')
async def add_user(user: UserAdd = Depends()) -> UserId:
    id = await UserRepository.add_user(user)
    return {"id": id}


@user_router.get('')
async def get_users() -> list[User]:
    users = await UserRepository.get_users()
    return users


@user_router.get('/{id}')
async def get_user(id: int) -> User:
    user = await UserRepository.add_user(id)
    return user


@quiz_router.post('')
async def add_qiuz(quiz: QuizAdd = Depends()) -> QuizId:
    id = await QuizRepository.add_quiz(quiz)
    return {'id': id}


@quiz_router.get('')
async def get_quizes() -> list[Quiz]:
    quizes = await QuizRepository.get_quizes()
    return quizes


@quiz_router.get('/{id}')
async def get_quiz(id: int) -> Quiz:
    quiz = await QuizRepository.get_quiz(id)
    return quiz


@question_router.post('')
async def add_question(question: QuestionAdd = Depends()) -> QuestionId:
    id = await QuestionRepository.add_quiz(question)
    return {'id': id}


@question_router.get('')
async def get_questions() -> list[Question]:
    questions = await QuestionRepository.get_questions()
    return questions


@question_router.get('/{id}')
async def get_question(id: int) -> Question:
    question = await QuestionRepository.get_question(id)
    return question


