from pydantic import BaseModel, ConfigDict


class UserAdd(BaseModel):
    name: str
    age: int
    phone: str | None = None


class User(UserAdd):
    id: int
    model_config = ConfigDict(from_atibutes=True)


class UserId(BaseModel):
    id: int


class QuizAdd(BaseModel):
    name: str
    user_id: int


class Quiz(QuizAdd):
    id: int
    model_config = ConfigDict(from_atibutes=True)


class QuizId(BaseModel):
    id: int


class QuestionAdd(BaseModel):
    question: str
    answer: str
    wrong1: str
    wrong2: str
    wrong3: str



class Question(QuestionAdd):
    id: int
    model_config = ConfigDict(from_atibutes=True)


class QuestionId(BaseModel):
    id: int
