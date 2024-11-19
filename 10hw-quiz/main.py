'''
Повторить проект с приложением QUIZ (папка flask2)
Добавить возможность:
    - просматривать все квизы и вопросы
    - добавлять квизы и вопросы
    - редактировать квизы и вопросы
    - удалять квизы и вопросы
    - изменять связи вопросов с квизами
'''

import os
from random import shuffle

from flask import Flask, render_template, url_for, redirect, request, flash, session
from models import *

BASE_FOLDER = os.getcwd()
app = Flask(__name__,
            static_folder=os.path.join(BASE_FOLDER, "static"),
            template_folder=os.path.join(BASE_FOLDER, "templates"))
app.config['SECRET_KEY'] = "my secret key - ds;ldks;ldks;ldks"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:120613@localhost:5432/fl_quiz"

db.init_app(app)

html_config = {
    'admin': True,
    'debug': False
}

with app.app_context():
    db_add_new_data()


@app.route('/')
def index():
    return render_template('base.html', html_config=html_config)


# выбор квеста
@app.route('/quiz/', methods=['GET', 'POST'])
def view_quiz():
    if request.method == 'GET':
        session['quiz_id'] = -1
        quizes = Quiz.query.all()
        return render_template('start.html', quizes=quizes, html_config=html_config)
    session['quiz_id'] = request.form.get('quiz')
    session['question_n'] = 0
    session['question_id'] = 0
    session['right_answers'] = 0
    return redirect(url_for('view_question'))


# прохождение квеста
@app.route('/question/', methods=['GET', 'POST'])
def view_question():
    if not session['quiz_id'] or session['quiz_id'] == -1:
        return redirect(url_for('view_quiz'))

    if request.method == 'POST':
        question = Question.query.filter_by(id=session['question_id']).one()
        if question.answer == request.form.get('ans_text'):
            session['right_answers'] += 1
        session['question_n'] += 1

    quiz = Quiz.query.filter_by(id=session['quiz_id']).one()

    if int(session['question_n']) >= len(quiz.question):
        session['quiz_id'] = -1
        return redirect(url_for('view_result'))
    else:
        question = quiz.question[session['question_n']]
        session['question_id'] = question.id
        answers = [question.answer, question.wrong1, question.wrong2, question.wrong3]
        shuffle(answers)
        return render_template('question.html',
                               answers=answers,
                               question=question,
                               html_config=html_config)


@app.route('/result/')
def view_result():
    return render_template('result.html',
                           right=session['right_answers'],
                           total=session['question_n'],
                           html_config=html_config)


@app.route('/quizes_view/', methods=['GET', 'POST'])
def view_quiz_edit():
    if request.method == 'POST':
        # q_name = request.form.get('name')
        #         # quiz = Quiz(q_name)
        #         # include_q = request.form.getlist('include_q')
        #         # for q in include_q:
        #         #     question = Question.query.get(q)
        #         #     print(question)
        #         #     quiz.question.append(question)
        #         # db.session.add(quiz)
        #         # db.session.commit()
        #         # return redirect(url_for('view_quiz_edit'))
        pass

    quizes = Quiz.query.all()
    questions = Question.query.all()
    return render_template('quizes_view.html',
                           html_config=html_config,
                           quizes=quizes,
                           questions=questions,
                           len=len)


@app.route('/quiz_add/', methods=['GET', 'POST'])
def quiz_add():
    questions = Question.query.all()
    if request.method == 'POST':
        action = request.form['action']
        if action == 'cancel':
            return redirect(url_for('view_quiz_edit'))
        elif action == 'save':
            quiz = Quiz(request.form.get('name'), User('user1'))
            include_q = request.form.getlist('include_q')
            for q in include_q:
                question = Question.query.get(q)
                print(question)
                quiz.question.append(question)
            db.session.add(quiz)
            db.session.commit()
            return redirect(url_for('view_quiz_edit'))

    return render_template('quiz_add.html', html_config=html_config, questions=questions)


# редактирование квеста
@app.route('/quiz_edit/<int:id>', methods=['GET', 'POST'])
def quiz_edit(id: int):
    quiz = Quiz.query.get(id)
    if request.method == 'GET':
        q_id = []
        for q in quiz.question:
            q_id.append(q.id)
        questions = Question.query.filter(Question.id.not_in(q_id)).all()

        return render_template('quiz_edit.html', quiz=quiz, html_config=html_config, questions=questions, is_add=False)

    action = request.form['action']
    if action == 'cancel':
        return redirect(url_for('view_quiz_edit'))
    elif action == 'delete':
        db.session.delete(quiz)
        db.session.commit()
        return redirect(url_for('view_quiz_edit'))
    elif action == 'save':
        # q_name = request.form.get('name')
        # print(q_name)
        quiz.name = request.form.get('name')
        exclude_q = request.form.getlist('exclude_q')
        include_q = request.form.getlist('include_q')
        for q in exclude_q:
            question = Question.query.get(q)
            print(question)
            quiz.question.remove(question)
        for q in include_q:
            question = Question.query.get(q)
            print(question)
            quiz.question.append(question)
        db.session.commit()
        return redirect(url_for('view_quiz_edit'))


@app.errorhandler(404)
def page_not_found(e):
    #snip
    return '<h1 style="color:red; text-align:center; margin-top:100px"> Упс..... </h1>'


app.run(debug=True)
