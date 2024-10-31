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
import os

from flask import Flask, render_template
import requests

BASE_FOLDER = os.getcwd()
print(BASE_FOLDER)
app = Flask(__name__,
            static_folder=os.path.join(BASE_FOLDER, "static"),
            template_folder=os.path.join(BASE_FOLDER, "templates"))
WeatherID = "af9a1c40b40d720ee1e352270cfc4e85"


def get_city_id(s_city: str) -> int:
    city_id = 0
    appid = WeatherID
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        city_id = data['list'][0]['id']

    except Exception as e:
        print("Exception (find):", e)
    return city_id


@app.route('/')
def index():
    return render_template('home_page.html')


@app.route('/duck/')
def duck():
    url = requests.get('https://random-d.uk/api/random').json()['url']
    return render_template('duck.html', url=url)


@app.route('/fox/<int:num>/')
def fox(num: int):
    if 1<=num<=10:
        urls = []
        for i in range(num):
            res = requests.get('https://randomfox.ca/floof/').json()
            urls.append(res['image'])
        return render_template('fox.html', urls=urls)
    else:
        return '<h1 style="color:red">Введите число от 1 до 10</h1>'



@app.route('/weather-minsk/')
def weather_msk():
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': 625144, 'units': 'metric', 'lang': 'ru', 'APPID': WeatherID})
        data = res.json()
    except Exception as e:
        print("Exception (weather):", e)
    return render_template('weather.html', city='Minsk', conditions=data['weather'][0]['description'],
                           temp=data['main']['temp'], feels_like=data['main']['feels_like'],
                           pressure=data['main']['pressure'], humidity=data['main']['humidity'])


@app.route('/weather/<string:city>/')
def weather(city: str):
    try:
        city_id = get_city_id(city)
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': WeatherID})
        data = res.json()
    except Exception as e:
        print("Exception (weather):", e)
    return render_template('weather.html', city=city, conditions=data['weather'][0]['description'],
                           temp=data['main']['temp'], feels_like=data['main']['feels_like'],
                           pressure=data['main']['pressure'], humidity=data['main']['humidity'])


@app.errorhandler(404)
def page_not_found(error):
    return '<h1 style="color:red">такой страницы не существует</h1>'


app.run(debug=True)