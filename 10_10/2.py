"""
Дан список пользователей след. формата:
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов.
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания.
Каждому пользователю с плохим логином вывести текст
"Уважаемый user_name, ваш логин user_login не является корректным."

"""
import re


def check_password(user: dict) -> bool:
    if len(user['password']) < 5:
        return False
    return True


def is_valid_login(user: dict) -> bool:
    if re.match(r'^[a-zA-Z0-9_]+$', user['login']):
        return True
    print(f"Уважаемый {user['name']}, ваш логин {user['login']} не является корректным.")
    return False


users = [
    {"name": "Alice", "login": "alice123", "password": "pass"},
    {"name": "Bob", "login": "bob_2021", "password": "password123"},
    {"name": "Charlie", "login": "charlie@", "password": "123"},
    {"name": "Dave", "login": "dave_smith", "password": "passw0rd"},
]

filter_by_password = list(filter(check_password, users))
# filter_by_password =  list(filter(lambda user: len(user['password']) >= 5, users))
filter_by_login = list(filter(is_valid_login,users))

print(filter_by_password)
print(filter_by_login)
