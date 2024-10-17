'''
создать класс Hero со след атрибутами:
    свойства:
        - name
        - health
        - armor
        - strong
    
    методы:
        - print_info - вывод информации о герое
        - kick - принимает параметр enemy:Hero и коэффициент силы удара  по дефолту равный 1,
                производит один удар - высчитывает и уменьшает броню и здоровье, 
                выводит информацию в консоль
        - fight - принимает параметр enemy:Hero и производит обмен ударами (поочереди или случайно)
                пока здоровье одного героя не достигнет 0 


                
Создать 2 героя, вывести информацию о них, произвести бой между ними, вывести информацию 
о победителе.

'''


class Hero:
    def __init__(self, name: str, health: int, armor: int, strong: int):
        self.name = name
        self.health = health
        self.armor = armor
        self.strong = strong

    # def __str__(self):
    #     return f'Имя: {self.name}\nЗдоровье: {self.health}\nБроня: {self.armor}\nСила: {self.strong}'

    def print_info(self):
        print(f'Имя: {self.name}\nЗдоровье: {self.health}\nБроня: {self.armor}\nСила: {self.strong}')
        # print(self)

    def kick(self, enemy: 'Hero', impact: int = 1):
        damage = impact * self.strong
        if enemy.armor >= damage:
            enemy.armor -= damage
        else:
            enemy.health -= (damage - enemy.armor)
            enemy.armor = 0
        print(f'{self.name} ударил {enemy.name} с силой {damage}. Теперь у {enemy.name} здоровье: {enemy.health}, '
              f'броня: {enemy.armor}.')

    def fight(self, enemy: 'Hero'):
        turn = 0
        while self.health > 0 and enemy.health > 0:
            if turn % 2 == 0:
                self.kick(enemy)
            else:
                enemy.kick(self)
            turn += 1
        winner = self if self.health > 0 else enemy
        print(f'{winner.name} победил!')


hero1 = Hero(name="Иван", health=100, armor=50, strong=20)
hero2 = Hero(name="Дракон", health=80, armor=60, strong=25)


hero1.print_info()
hero2.print_info()

hero1.fight(hero2)
