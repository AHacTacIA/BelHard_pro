'''
Написать программу-сервер принимающую http запросы и
отдающую в ответ html-файл или файл картинку указанный в пути запроса.
Если запрос на главную страницу - вернуть заголовок h2 - Главная страница.
Если файла нет - выдать ошибку 404

'''

import socket
import re


def send_file(file, conn):
    try:
        with open(file.lstrip('/'), 'rb') as fl:
            conn.send(OK)
            conn.send(fl.read())

    except IOError:
        conn.send(ERR_404)


def read_file(file):
    try:
        with open(file.lstrip('/'), 'rb') as fl:
            return [OK, fl.read()]
    except FileNotFoundError:
        return [ERR_404, b'<html><head><title>404 Not Found</title></head><body><h2>404 File Not '
                         b'Found</h2></body></html>']


def is_file(path: str) -> bool:
    if re.match(r'^.*\.(jpg|png|gif|ico|html)$', path):
        return True
    return False


def handle_request(path: str):
    if path == '/':
        response, contetnt = read_file('main_page.html')
        response += contetnt
    elif is_file(path):
        response, content = read_file(path)
        response += content
    else:
        _, content = read_file('error_page.html')
        response = ERR_404 + content
    return response


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # определили tcp/ip

HOST = ('127.0.0.1', 7777)
sock.bind(HOST)
sock.listen()

path = ''

OK = b'HTTP/1.1 200 OK\n\n'
ERR_404 = b'HTTP/1.1 404 Not Found\n\n'

while 1:
    print('Listen....')
    conn, addr = sock.accept()  # зависаем в ожидании
    data = conn.recv(4096).decode()  # принимаем данные по 4 КБайт

    try:
        path = data.split('\n')[0].split()[1]  # получаем path из 1ой строки http
        response = handle_request(path)
        conn.sendall(response)
    except:
        conn.send(b'no http')

    conn.close()
