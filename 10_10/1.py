"""
Написать функцию printn() которая будет печатать переданный текст,
но при этом перед этим текстом выводить строку с номером отражающим
кокай раз по счету выполняется эта функция.

"""

def printn(text: str) -> None:
    global n
    n += 1
    print(n)
    print(text)

n=0
printn('Hello')
printn('World')