import re
import requests
from model import *

WeatherID = "af9a1c40b40d720ee1e352270cfc4e85"


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


def check_name(name: str, errors: list) -> bool:
    if not re.match(r'^[а-яА-ЯёЁ\s]+$', name):
        errors.append("Имя и фамилия должны содержать только русские буквы")
        return False
    return True


def check_login(login: str, errors: list) -> bool:
    if not re.match(r'^[a-zA-Z0-9_]{6,20}$', login):
        errors.append("Логин должен содержать латинские буквы, цифры, _ и быть длиной от 6 до 20 символов")
        return False
    if find_user_by_login(login):
        errors.append("Пользователь с таким логином уже существует")
        return False
    return True


def check_password(password: str, errors: list) -> bool:
    if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,15}$', password):
        errors.append(
            "Пароль должен содержать хотя бы 1 строчную букву, 1 заглавную букву и 1 цифру и быть длиной от 8 до 15 символов")
        return False
    return True


def check_email(email: str, errors: list) -> bool:
    if not re.match(r'^\S+@\S+\.\S+$', email):
        errors.append("Email должен быть валидным")
        return False
    if find_user_by_email(email):
        errors.append("Пользователь с таким email уже существует")
        return False
    return True


def check_age(age: int, errors: list) -> bool:
    try:
        age = int(age)
        if age < 12 or age > 100:
            errors.append("Возраст должен быть целым числом от 12 до 100")
            return False
    except ValueError:
        errors.append("Возраст должен быть целым числом от 12 до 100")
    return True


def get_weather(city_id: int):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': WeatherID})
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print("Exception (weather):", e)
        return None
