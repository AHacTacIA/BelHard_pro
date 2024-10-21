from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine("postgresql://postgres:120613@localhost:5432/users", echo=True)


class Base(DeclarativeBase):
    pass


# Define the User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


# Create the table
Base.metadata.create_all(engine)

# Session setup
Session = sessionmaker(bind=engine)
session = Session()


def add_user(login:str, password:str):
    new_user = User(login=login, password=password)
    session.add(new_user)
    try:
        session.commit()
        print(f"Пользователь {login} зарегистрирован")
    except Exception as e:
        session.rollback()
        print(f"Ошибка регистрации: {e}")


def find_user_by_login(login:str)->bool:
    user = session.query(User).filter_by(login=login).first()
    if user:
        return True
    else:
        return False
