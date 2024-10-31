"""
Добавить в проект прошлого задания шаблоны. 

На главной странице сделать ссылки на каждый ендпоинт

На каждой неглавной странице сделать кнопку-ссылку - возврат на главную страницу

Добавить страницу с картинкой и счетчиком кликов по ней. 
    На главной странице  добавить ссылку  на нее 

На главной странице добавить ссылку на страницу с погодой 5 разных городов, 
    которая будет отображаться если запрос пришел на сервер в четную минуту 
    текущего времени. 
    т.е. 10:52 - ссылка отображается на главной странице, 10:51 - нет
    если пользователь сам вбивает адрес этой страницы - тоже делать проверку
    

"""
import datetime
import os

from flask import Flask, render_template, url_for, redirect, request
import requests

BASE_FOLDER = os.getcwd()
print(BASE_FOLDER)
app = Flask(__name__,
            static_folder=os.path.join(BASE_FOLDER, "static"),
            template_folder=os.path.join(BASE_FOLDER, "templates"))
WeatherID = "af9a1c40b40d720ee1e352270cfc4e85"
cl_num = 0


def get_city_id(s_city: str) -> int:
    city_id = 0
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': WeatherID})
        data = res.json()
        city_id = data['list'][0]['id']

    except Exception as e:
        print("Exception (find):", e)
    return city_id


def get_weather(city_id: int):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': WeatherID})
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print("Exception (weather):", e)
        return None


@app.route('/')
def index():
    current_minute = datetime.datetime.now().minute
    return render_template('home_page.html', display_link=current_minute % 2 == 0)


@app.route('/duck/')
def duck():
    url = requests.get('https://random-d.uk/api/random').json()['url']
    return render_template('duck.html', url=url)


@app.route('/fox/<int:num>/')
def fox(num: int):
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
    data = get_weather(625144)
    return render_template('weather.html', weather=data)


@app.route('/weather/<string:city>/')
def weather(city: str):
    city_id = get_city_id(city)
    data = get_weather(city_id)
    return render_template('weather.html', weather=data)


@app.route('/weather-reg/')
def weather_reg():
    current_minute = datetime.datetime.now().minute
    if current_minute % 2 != 0:
        return redirect(url_for('index'))
    city_ids = [625144, 629634, 620127, 627907, 627904, 625665]  #ID областных центров РБ
    weather_data = [get_weather(city_id) for city_id in city_ids]
    return render_template('weather_reg.html', weather_data=weather_data)


@app.route('/clicker/', methods=['GET','POST'])
def clicker():
    global cl_num
    if request.method == 'POST':
        cl_num += 1
    return render_template('clicker.html', num=cl_num)


@app.errorhandler(404)
def page_not_found(error):
    return '<h1 style="color:red">такой страницы не существует</h1>'


app.run(debug=True)
