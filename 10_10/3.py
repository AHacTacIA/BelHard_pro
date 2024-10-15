"""
Дан словарь наблюдения за температурой
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}.
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""
temperature = {"day1": 18, "day2": 22, "day3": 7, "day4": 11, "day5": 14}

# Сортировка по возрастанию
sorted_asc = dict(sorted(temperature.items(), key=lambda item: item[1]))
print("По возрастанию:", sorted_asc)

# Сортировка по убыванию
sorted_desc = dict(sorted(temperature.items(), key=lambda item: item[1], reverse=True))
print("По убыванию:", sorted_desc)
