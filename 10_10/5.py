'''

Дан списк:
['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
Для каждого элемента в списке
    - вывести на экран сначала номер элемента
    - сам элемент
    - символ данного элемента, соответствующий номеру его позиции в списке.
Образец:
1 - qwertyu - q
2 - asdfggh - s
3 - zxcvbnm - c
и так далее...


'''

strings = ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
for i, item in enumerate(strings, start=0):
    print(f'{i+1} - {item} - {item[i]}')