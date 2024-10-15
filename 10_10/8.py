'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы
 - остались только строки.
 - остался только логический тип.

'''

mixed_list = ['hello', 123, True, 45.6, 'world', False, None, 1]
str_list = list(filter(lambda item: type(item) is str, mixed_list))
bool_list = list(filter(lambda item: type(item) is bool, mixed_list))
print(str_list)
print(bool_list)
