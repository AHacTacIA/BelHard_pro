from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import select, String, ForeignKey, Table, Column, Integer
from schema import UserAdd, QuizAdd, QuestionAdd

# engine = create_async_engine("sqlite+aiosqlite:///db//fastapi.db")
engine = create_async_engine("postgresql+asyncpg://postgres:120613@localhost:5432/api_quiz")
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


quiz_question = Table(
    'quiz_question', Model.metadata,
    Column('quiz_id', Integer, ForeignKey('quiz.id'), primary_key=True),
    Column('question_id', Integer, ForeignKey('question.id'), primary_key=True))


class UserOrm(Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int]
    phone: Mapped[str | None]
    quizes: Mapped[list["QuizOrm"]] = relationship("QuizOrm", back_populates="user", cascade="all, delete, delete-orphan")


class QuizOrm(Model):
    __tablename__ = 'quiz'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped["UserOrm"] = relationship("UserOrm", back_populates="quizes")
    question: Mapped[list["QuestionOrm"]] = relationship("QuestionOrm", secondary=quiz_question,back_populates="quizes")


class QuestionOrm(Model):
    __tablename__ = 'question'
    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column(String(250))
    answer: Mapped[str] = mapped_column(String(100))
    wrong1: Mapped[str] = mapped_column(String(100))
    wrong2: Mapped[str] = mapped_column(String(100))
    wrong3: Mapped[str] = mapped_column(String(100))
    quizes: Mapped[list["QuizOrm"]] = relationship("QuizOrm", secondary=quiz_question, back_populates="question")


# user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def add_test_data():
    async with new_session() as session:
        users = [
            UserOrm(name='user1', age=11),
            UserOrm(name='user2', age=22, phone='1234567'),
            UserOrm(name='user3', age=33)
        ]

        quizes = [
            QuizOrm(name='QUIZ 1', user_id=users[0].id),
            QuizOrm(name='QUIZ 2', user_id=users[1].id),
            QuizOrm(name='QUIZ 3', user_id=users[2].id),
            QuizOrm(name='QUIZ 4', user_id=users[2].id)

        ]

        questions = [
            QuestionOrm(question='Сколько будут 2+2*2', answer='6', wrong1='8', wrong2='2', wrong3='0'),
            QuestionOrm(question='Сколько месяцев в году имеют 28 дней?', answer='Все', wrong1='Один',
                        wrong2='Ни одного', wrong3='Два'),
            QuestionOrm(question='Каким станет зелёный утёс, если упадет в Красное море?', answer='Мокрым',
                        wrong1='Красным', wrong2='Не изменится',
                        wrong3='Фиолетовым'),
            QuestionOrm(question='Какой рукой лучше размешивать чай?', answer='Ложкой', wrong1='Правой', wrong2='Левой',
                        wrong3='Любой'),
            QuestionOrm(question='Что не имеет длины, глубины, ширины, высоты, а можно измерить?', answer='Время',
                        wrong1='Глупость', wrong2='Море',
                        wrong3='Воздух'),
            QuestionOrm(question='Когда сетью можно вытянуть воду?', answer='Когда вода замерзла',
                        wrong1='Когда нет рыбы',
                        wrong2='Когда уплыла золотая рыбка', wrong3='Когда сеть порвалась'),
            QuestionOrm(question='Что больше слона и ничего не весит?', answer='Тень слона', wrong1='Воздушный шар',
                        wrong2='Парашют', wrong3='Облако'),
            QuestionOrm(question='Что такое у меня в кармашке?', answer='Кольцо', wrong1='Кулак', wrong2='Дырка',
                        wrong3='Бублик')
        ]

        quizes[0].question.append(questions[0])
        quizes[0].question.append(questions[1])
        quizes[0].question.append(questions[2])

        quizes[1].question.append(questions[3])
        quizes[1].question.append(questions[4])
        quizes[1].question.append(questions[5])
        quizes[1].question.append(questions[6])
        quizes[1].question.append(questions[0])

        quizes[2].question.append(questions[7])
        quizes[2].question.append(questions[6])
        quizes[2].question.append(questions[5])
        quizes[2].question.append(questions[4])

        quizes[3].question.append(questions[6])
        quizes[3].question.append(questions[0])
        quizes[3].question.append(questions[1])
        quizes[3].question.append(questions[3])
        # session.add_all(users)

        # session.add_all(quizes)
        session.add_all(questions)
        await session.commit()

class UserRepository:

    @classmethod
    async def add_user(cls, user: UserAdd) -> int:
        async with new_session() as session:
            data = user.model_dump()
            user = UserOrm(**data)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id

    @classmethod
    async def get_users(cls) -> list[UserOrm]:
        async with new_session() as session:
            query = select(UserOrm)
            res = await session.execute(query)
            users = res.scalars().all()
            return users

    @classmethod
    async def get_user(cls, id: int) -> UserOrm:
        async with new_session() as session:
            query = select(UserOrm).filter(UserOrm.id == id)
            # query = text("select int_id from table")
            res = await session.execute(query)
            user = res.scalars().first()  # scalar - преобр в список
            return user


class QuizRepository:

    @classmethod
    async def add_quiz(cls, quiz: QuizAdd) -> int:
        async with new_session() as session:
            data = quiz.model_dump()
            quiz = QuizOrm(**data)
            session.add(quiz)
            await session.flush()
            await session.commit()
            return quiz.id

    @classmethod
    async def get_quizes(cls) -> list[QuizOrm]:
        async with new_session() as session:
            query = select(QuizOrm)
            res = await session.execute(query)
            quizes = res.scalars().all()
            return quizes

    @classmethod
    async def get_quiz(cls, id: int) -> QuizOrm:
        async with new_session() as session:
            query = select(QuizOrm).filter(QuizOrm.id == id)
            res = await session.execute(query)
            quiz = res.scalars().first()
            return quiz


class QuestionRepository:

    @classmethod
    async def add_question(cls, question: QuestionAdd) -> int:
        async with new_session() as session:
            data = question.model_dump()
            question = QuestionOrm(**data)
            session.add(question)
            await session.flush()
            await session.commit()
            return question.id

    @classmethod
    async def get_questions(cls) -> list[QuestionOrm]:
        async with new_session() as session:
            query = select(QuestionOrm)
            res = await session.execute(query)
            questions = res.scalars().all()
            return questions

    @classmethod
    async def get_question(cls, id: int) -> QuestionOrm:
        async with new_session() as session:
            query = select(QuestionOrm).filter(QuestionOrm.id == id)
            res = await session.execute(query)
            question = res.scalars().first()
            return question
