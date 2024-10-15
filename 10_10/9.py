'''
1. Написать функцию, которая принимает некоторые данные пользователя
с помощью (**kwargs). Если есть данные с именем(name) или фамилией(surname)
или возрастом(age), распечатать информацию о пользователе используя присутствующие
из этих трех параметров, иначе вывести сообщение о том, что нужных данных нет.
'''


def user_info(**kwargs):
    if 'name' in kwargs or 'surname' in kwargs or 'age' in kwargs:
        if 'name' in kwargs:
            print(f'Имя: {kwargs["name"]}')
        if 'surname' in kwargs:
            print(f'Фамилия: {kwargs["surname"]}')
        if 'age' in kwargs:
            print(f'Возраст: {kwargs["age"]}')
    else:
        print('Данных нет')


user_info(name="Иван",  age=25)
user_info()
