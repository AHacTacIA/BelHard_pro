"""

написать приложение-клиент используя модуль socket работающее в домашней 
локальной сети.
Приложение должно соединятся с сервером по известному адрес:порт и отправлять 
туда текстовые данные.

известно что сервер принимает данные следующего формата:
    "command:reg; login:<login>; password:<pass>" - для регистрации пользователя
    "command:signin; login:<login>; password:<pass>" - для входа пользователя
    
    
с помощью программы зарегистрировать несколько пользователей на сервере и произвести вход
"""

import socket

sock = socket.socket()

HOST = ('127.0.0.1', 7777)

sock.connect(HOST) # соединяемся с сервером указывая его адрес и порт
command = int(input('Enter 1 for registration\n'
                    'Enter 2 for sign in\n'))
login = input('Enter login: ')
password = input('Enter password: ')
if command == 1:
    sock.send(f'command:reg; login:{login}; password:{password}'.encode('utf-8'))
elif command == 2:
    sock.send(f'command:signin; login:{login}; password:{password}'.encode('utf-8'))
