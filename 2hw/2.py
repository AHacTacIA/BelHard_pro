'''
создать классы Mage, Knight, Ork унаследовав его от Hero
    новые свойства:
        - special_points - количество спец очков
        - special_points_name - мана, доблесть, ярость
        - special_points_k - коэффициент (множитель ) увеличивающий обычную атаку
    
    новые методы:
        - hello - приветственное сообщение с выводом информации   
        - special_attack - этом удар производится с использованием коэффициента.
                При спец атаке вычитать из спец.очков 1. Невозможен если очков нет.
        - attack - с вероятностью 25% будет использовать спец.способность героя 
                если у него остались спец.очки. Если вероятность пришлась на
                остальные 75% - выполнить обычную атаку. 
                Вывести сообщение в консоль о типе и результате атаки.
        
        

добавить класс Arena:
        - атрибут warriors - все воины на арене (тип list)
        - магический метод __init__, который принимает необязательный аргумент warriors.
                Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
                пустым списком.
        - метод add_warrior, который принимает аргумент warrior и добавляет его к warriors.
                Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
                Если нет, то добавить воина к списку warriors и вывести сообщение на экран
                "{warrior.name} участвует в битве"        
        - метод battle, который не принимает аргументов и симулирует битву. Сперва 
                должна пройти проверка, что воинов на арене больше 1. Если меньше, то бросить
                исключение ValueError("Количество воинов на арене должно быть больше 1").
                Битва продолжается, пока на арене не останется только один воин. Сперва
                в случайном порядке выбираются атакующий и защищающийся. Атакующий ударяет
                защищающегося. Если у защищающегося осталось 0 health_points, то удалить его
                из списка воинов и вывести на экран сообщение "{defender.name} пал в битве".
                Когда останется только один воин, то вывести сообщение "Победил воин: {winner.name}".
                Вернуть данного воина из метода battle. 
             
             
Создать несколько воинов используя разные классы, добавить их на арену и запустить битву. 
Выжить должен только один.                
'''
import random

from hero import Hero


class Mage(Hero):
    def __init__(self, name: str, health: float, armor: float, strong: float, special_points: float,
                 special_points_k: float):
        super().__init__(name, health, armor, strong)
        self.special_points = special_points
        self.special_points_name = 'Мана'
        self.special_points_k = special_points_k

    def hello(self):
        """Приветственное сообщение с выводом информации"""
        print(f'Я {self.name}, могучий маг! У меня {self.special_points} {self.special_points_name}.')

    def special_attack(self, enemy: Hero):
        """Этот удар производится с использованием коэффициента.
                При спец атаке вычитать из спец.очков 1. Невозможен если очков нет"""
        if self.special_points > 0:
            self.special_points -= 1
            self.kick(enemy, self.special_points_k)
            print(f'{self.name} использует спец атаку!')

    def attack(self, enemy: Hero):
        """С вероятностью 25% будет использовать спец.способность героя
                если у него остались спец.очки. Если вероятность пришлась на
                остальные 75% - выполнить обычную атаку.
                Вывести сообщение в консоль о типе и результате атаки."""
        if random.random() <= 0.25 and self.special_points > 0:
            self.special_attack(enemy)
        else:
            self.kick(enemy)


class Knight(Hero):
    def __init__(self, name: str, health: float, armor: float, strong: float, special_points: float,
                 special_points_k: float):
        super().__init__(name, health, armor, strong)
        self.special_points = special_points
        self.special_points_name = 'Доблесть'
        self.special_points_k = special_points_k

    def hello(self):
        """Приветственное сообщение с выводом информации"""
        print(f'Я {self.name}, доблестный рыцарь! У меня {self.special_points} {self.special_points_name}.')

    def special_attack(self, enemy: Hero):
        """Этот удар производится с использованием коэффициента.
                При спец атаке вычитать из спец.очков 1. Невозможен если очков нет"""
        if self.special_points > 0:
            self.special_points -= 1
            self.kick(enemy, self.special_points_k)
            print(f'{self.name} использует спец атаку!')

    def attack(self, enemy: Hero):
        """С вероятностью 25% будет использовать спец.способность героя
                если у него остались спец.очки. Если вероятность пришлась на
                остальные 75% - выполнить обычную атаку.
                Вывести сообщение в консоль о типе и результате атаки."""
        if random.random() <= 0.25 and self.special_points > 0:
            self.special_attack(enemy)
        else:
            self.kick(enemy)


class Ork(Hero):
    def __init__(self, name: str, health: float, armor: float, strong: float, special_points: float,
                 special_points_k: float):
        super().__init__(name, health, armor, strong)
        self.special_points = special_points
        self.special_points_name = 'Ярость'
        self.special_points_k = special_points_k

    def hello(self):
        """Приветственное сообщение с выводом информации"""
        print(f'Я {self.name}, яростный орк! У меня {self.special_points} {self.special_points_name}.')

    def special_attack(self, enemy: Hero):
        """Этот удар производится с использованием коэффициента.
                При спец атаке вычитать из спец.очков 1. Невозможен если очков нет"""
        if self.special_points > 0:
            self.special_points -= 1
            self.kick(enemy, self.special_points_k)
            print(f'{self.name} использует спец атаку!')

    def attack(self, enemy: Hero):
        """С вероятностью 25% будет использовать спец.способность героя
                если у него остались спец.очки. Если вероятность пришлась на
                остальные 75% - выполнить обычную атаку.
                Вывести сообщение в консоль о типе и результате атаки."""
        if random.random() <= 0.25 and self.special_points > 0:
            self.special_attack(enemy)
        else:
            self.kick(enemy)


class Arena:
    def __init__(self, warriors: list = []):
        """
        Принимает необязательный аргумент warriors.
            Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
            пустым списком.
        """
        self.warriors = warriors

    def add_warrior(self, warrior: [Mage, Knight, Ork]):
        """
        Принимает аргумент warrior и добавляет его к warriors.
                Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
                Если нет, то добавить воина к списку warriors и вывести сообщение на экран
                "{warrior.name} участвует в битве"
        """
        if warrior in self.warriors:
            raise ValueError('Воин уже на арене')
        self.warriors.append(warrior)
        print(f'{warrior.name} участвует в битве')

    def battle(self):
        """
        Не принимает аргументов и симулирует битву.
            Сперва должна пройти проверка, что воинов на арене больше 1.
            Если меньше, то бросить исключение ValueError("Количество воинов на арене должно быть больше 1").
            Битва продолжается, пока на арене не останется только один воин. Сперва в случайном порядке
            выбираются атакующий и защищающийся. Атакующий ударяет защищающегося.
            Если у защищающегося осталось 0 health_points, то удалить его из списка воинов и вывести на экран сообщение
            "{defender.name} пал в битве". Когда останется только один воин, то вывести сообщение
            "Победил воин: {winner.name}". Вернуть данного воина из метода battle.
        """
        if len(self.warriors) <= 1:
            raise ValueError('Количество воинов на арене должно быть больше 1')
        while len(self.warriors) > 1:
            attacker, defender = random.sample(self.warriors, 2)
            attacker.attack(defender)
            if defender.health <= 0:
                self.warriors.remove(defender)
                print(f'{defender.name} пал в битве')
        winner = self.warriors[0]
        print(f'Победил воин: {winner.name}')
        return winner


# Пример использования
arena = Arena()
mage = Mage(name='Гэндальф', health=100, armor=50, strong=20, special_points=5, special_points_k=1.5)
knight = Knight(name='Артур', health=120, armor=70, strong=25, special_points=3, special_points_k=1.3)
ork = Ork(name='Горук', health=150, armor=60, strong=30, special_points=4, special_points_k=2.)

arena.add_warrior(mage)
arena.add_warrior(knight)
arena.add_warrior(ork)

winner = arena.battle()
