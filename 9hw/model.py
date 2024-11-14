# from flask_sqlalchemy import SQLAlchemy
from _main import db, app


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False)
    login = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'User {self.username}'


def add_user(username, login, email, password, age):
    with app.app_context():
        new_user = User(username=username, login=login, email=email, password=password, age=age)
        db.session.add(new_user)
        db.session.commit()
        print(f"User {username} added successfully!")


def remove_user(user_id):
    with app.app_context():
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            print(f"User {user.username} removed successfully!")
        else:
            print("User not found.")


def find_user_by_login(login):
    with app.app_context():
        user = User.query.filter_by(login=login).first()
        if user:
            return user
        else:
            print("User not found.")
            return None


def find_user_by_email(email):
    with app.app_context():
        user = User.query.filter_by(email=email).first()
        if user:
            return user
        else:
            print("User not found.")
            return None
