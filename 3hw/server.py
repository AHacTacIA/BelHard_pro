"""
Написать приложение-сервер используя модуль socket работающее в домашней
локальной сети.
Приложение должно принимать данные с любого устройства в сети отправленные
или через программу клиент или через браузер
    - если данные пришли по протоколу http создать возможность след.логики:
        - если путь содержит /test/<int>/ вывести сообщение - тест с номером int запущен

        - если путь содержит message/<login>/<text>/ вывести в консоль сообщение
            "{дата время} - сообщение от пользователя {login} - {text}"

        - во всех остальных случаях вывести сообщение:
            "пришли неизвестные  данные по HTTP - путь такой то"


    - если данные пришли НЕ по протоколу http создать возможность след.логики:
        - если пришла строка формата "command:reg; login:<login>; password:<pass>"
            - выполнить проверку:
                login - только латинские символы и цифры, минимум 6 символов
                password - минимум 8 символов, должны быть хоть 1 цифра
            - при успешной проверке:
                1. вывести сообщение:
                    "{дата время} - пользователь {login} зарегистрирован"
                2. добавить данные пользователя в список/словарь
            - если проверка не прошла вывести сообщение:
                "{дата время} - ошибка регистрации {login} - неверный пароль/логин"

        - если пришла строка формата "command:signin; login:<login>; password:<pass>"
            выполнить проверку зарегистрирован ли такой пользователь:

            при успешной проверке:
                1. вывести сообщение:
                    "{дата время} - пользователь {login} произведен вход"

            если проверка не прошла вывести сообщение
                "{дата время} - ошибка входа {login} - неверный пароль/логин"

        - во всех остальных случаях вывести сообщение:
            "пришли неизвестные  данные - <присланные данные>"


"""
import socket
import re
from datetime import datetime
from model import *


def http_path(path: str):
    test_match = re.match(r'^/test/(\d+)/$', path)
    message_match = re.match(r'^/message/([^/]+)/([^/]+)/$', path)

    if test_match:
        test_number = test_match.group(1)
        print(f'Тест с номером {test_number} запущен')
    elif message_match:
        login = message_match.group(1)
        text = message_match.group(2)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f'{current_time} - сообщение от пользователя {login} - {text}')
    else:
        print(f'пришли неизвестные данные по HTTP - путь: {path}')


def user_validation(input_string: str):
    """
        - если пришла строка формата "command:reg; login:<login>; password:<pass>"
            - выполнить проверку:
                login - только латинские символы и цифры, минимум 6 символов
                password - минимум 8 символов, должны быть хоть 1 цифра
            - при успешной проверке:
                1. вывести сообщение:
                    "{дата время} - пользователь {login} зарегистрирован"
                2. добавить данные пользователя в список/словарь
            - если проверка не прошла вывести сообщение:
                "{дата время} - ошибка регистрации {login} - неверный пароль/логин"

        - если пришла строка формата "command:signin; login:<login>; password:<pass>"
            выполнить проверку зарегистрирован ли такой пользователь:

            при успешной проверке:
                1. вывести сообщение:
                    "{дата время} - пользователь {login} произведен вход"

            если проверка не прошла вывести сообщение
                "{дата время} - ошибка входа {login} - неверный пароль/логин"
    """

    reg_match = re.match(r'^command:reg; login:([^;]+); password:([^;]+);?$', input_string)
    signin_match = re.match(r'^command:signin; login:([^;]+); password:([^;]+);?$', input_string)
    if reg_match:
        login = reg_match.group(1)
        password = reg_match.group(2)
        if re.match(r'^[a-zA-Z0-9]{6,}$', login) and len(password) >= 8 and re.search(r'\d', password):
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if find_user_by_login(login):
                print(f'{current_time} - ошибка регистрации {login} - пользователь уже зарегистрирован')
            else:
                add_user(login, password)
                print(f'{current_time} - пользователь {login} зарегистрирован')
        else:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'{current_time} - ошибка регистрации {login} - неверный пароль/логин')
    elif signin_match:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        login = signin_match.group(1)
        if find_user_by_login(login):
            print(f'{current_time} - пользователь {login} произведен вход')
        else:
            print(f'{current_time} - ошибка входа {login} - неверный пароль/логин')
    else:
        print(f'Пришли неизвестные данные - {input_string}')


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # определили tcp/ip

HOST = ('127.0.0.1', 7777)

sock.bind(HOST)
sock.listen()

# HTTP
# GET /project1/test1/ HTTP/1.1 - первая строка определяющая что это http - 3 параметра разделенные пробелом (тип путь протокол)
# Host: some.ru - 2я и последующие строки заголовки

path = ''

while 1:
    conn, addr = sock.accept()  # зависаем в ожидании
    data = conn.recv(1024).decode()  # принимаем данные по 1 КБайту
    http = data.split('\n')[0].split()[2].split('/')[0]
    if http == 'HTTP':
        path = data.split('\n')[0].split()[1]  # получаем path из 1ой строки http
        http_path(path)
    else:
        user_validation(data)
