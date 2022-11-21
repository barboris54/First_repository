# def decor(tx=None, decor_text=''):
#     def wrapper(fn):
#         def wrap(*args):
#             print(decor_text, end='')
#             fn(*args)
#
#         return wrap
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
#
# @decor
# def hello_world(text):
#     print(text)
#
#
# @decor(decor_text='hello')
# def hello_world2(text):
#     print(text)
#
#
# hello_world2('Hi')
# hello_world('world!')

# print(bin(18))
# print(oct(18))

# q = 'pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
# print('y' in e)
#
# def changeChar(s, simb, new_simb):
#     new_str = ''
#     for i in s:
#         if i != simb:
#             new_str += i
#         else:
#             new_str += new_simb
#     return new_str
#
#
# str1 = 'Я изучаю Nuyhon. Мне нравится Nuthon. Nuthon очень интресный язык программирования'
# str2 = changeChar(str1, 'N', 'P')
# print(str2)

# print(u'Hello')
# print(r'C:\file.txt\\'[:-1])

# s = """
#     <div>
#         <a href = '#'>content</a>
#     <\div>"""
# print(s)

# def square(n):
#     """Принимает число и возводит его во вторую степень"""
#     return n**2
#
# print(square(5))
# print(square.__doc__)

import math


def cylinder(r, h):
    """
    Вычисляет площадь цилиндра.

    Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
    :param r: положительное число, радиус основания цилиндра
    :param h: положительное число, выстоа цилиндра
    :return: положительное число, площадь цилидра
    """
    return 2 * math.pi * r * (r + h)

print(cylinder(2,4))
