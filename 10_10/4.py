'''
Дан список [1,2,3,4,5,6,7,8,9]. Создать 3 копии этого списка
и с каждой выполнить след действия:
    - возвести каждый элемент во 2ю степень
    - прибавить 3 к каждому элементу значение которого является четным
    - элементы значения которого является
            четными - умножить на 2
            нечетным - умножить на 3

Использовать map и lambda.
'''
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array1 = list(map(lambda num: num ** 2, array))
array2 = list(map(lambda num: num + 3 if num % 2 == 0 else num, array))
array3 = list(map(lambda num: num * 2 if num % 2 == 0 else num * 3, array))
print(array)
print(array1)
print(array2)
print(array3)
