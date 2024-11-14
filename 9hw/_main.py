import datetime
import os

from flask import Flask, render_template, url_for, redirect, request, flash, session
from flask_sqlalchemy import SQLAlchemy

from func import *

BASE_FOLDER = os.getcwd()

app = Flask(__name__,
            static_folder=os.path.join(BASE_FOLDER, "static"),
            template_folder=os.path.join(BASE_FOLDER, "templates"))
app.config['SECRET_KEY'] = "my secret key - ds;ldks;ldks;ldks"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:120613@localhost:5432/fl_users"

db = SQLAlchemy(app)





@app.route('/')
def index():
    current_minute = datetime.datetime.now().minute
    if 'click_count' not in session:
        session['click_count'] = 0
    return render_template('home_page.html', display_link=current_minute % 2 == 0)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # session['click_count'] = 0
        login = request.form.get('login')  # запрос к данным формы
        password = request.form.get('password')
        user = find_user_by_login(login)
        if user:
            if user.password != password:
                message = 'Неверный логин или пароль'
                return render_template('login.html', message=message, login=login)
            session['user_id'] = user.id
            session['username'] = user.username
        else:
            message = 'Неверный логин'
            return render_template('login.html', message=message, login=login)

        return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        login = request.form['login']
        email = request.form['email']
        password = request.form['password']
        age = request.form['age']
        errors = []

        # Проверка имени и фамилии (только русские буквы)
        check_name(username, errors)

        # Проверка логина (латинские буквы, цифры, _ , от 6 до 20 символов)
        check_login(login, errors)

        # Проверка пароля (1 строчная, 1 заглавная, 1 цифра, от 8 до 15 символов)
        check_password(password, errors)

        # Проверка email (валидный email)
        check_email(email, errors)

        # Проверка возраста (целое число от 12 до 100)
        check_age(age, errors)

        if errors:
            for error in errors:
                flash(error)
            return render_template('register.html', username=username, login=login, email=email, age=age)
        else:
            add_user(username, login, email, password, age)
            return redirect(url_for('index'))

    return render_template('register.html')


@app.route('/duck/')
def duck():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    url = requests.get('https://random-d.uk/api/random').json()['url']
    return render_template('duck.html', url=url)


@app.route('/fox/<int:num>/')
def fox(num: int):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if 1 <= num <= 10:
        urls = []
        for i in range(num):
            res = requests.get('https://randomfox.ca/floof/').json()
            urls.append(res['image'])
        return render_template('fox.html', urls=urls)
    else:
        return '<h1 style="color:red">Введите число от 1 до 10</h1>'


@app.route('/weather-minsk/')
def weather_msk():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    data = get_weather(625144)
    return render_template('weather.html', weather=data)


@app.route('/weather/<string:city>/')
def weather(city: str):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    city_id = get_city_id(city)
    data = get_weather(city_id)
    return render_template('weather.html', weather=data)


@app.route('/weather-reg/')
def weather_reg():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    current_minute = datetime.datetime.now().minute
    if current_minute % 2 != 0:
        return redirect(url_for('index'))
    city_ids = [625144, 629634, 620127, 627907, 627904, 625665]  #ID областных центров РБ
    weather_data = [get_weather(city_id) for city_id in city_ids]
    return render_template('weather_reg.html', weather_data=weather_data)


@app.route('/clicker/', methods=['GET', 'POST'])
def clicker():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        session['click_count'] += 1
    return render_template('clicker.html', num=session['click_count'])


@app.route('/home_work/')
def hw8():
    return render_template('8hw.html')


@app.errorhandler(404)
def page_not_found(error):
    return '<h1 style="color:red">такой страницы не существует</h1>'


app.run(debug=True)
