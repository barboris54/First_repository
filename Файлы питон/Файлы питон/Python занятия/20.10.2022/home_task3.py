# # Задание № 1
import math


# def mult(*args):
#     res = math.prod(args)
#     return res
#
#
# print(mult(9,10))
# print(mult(2,3,4))
# print(mult(3,5,10,6))

# Задание № 2

# def fibonaci(*args):
#     summa = 0
#     for i in args:
#         summa += i
#         print(summa, end=' ')
#     print()
#
# fibonaci(3,9,1,)
# fibonaci(2,7,11,13)

# Задание № 3

def square(figure, **kwargs):
    if figure == 'rhombus':
        values = list(kwargs.values())
        return (values[0] * values[1] / 2)
    if figure == 'square':
        values = list(kwargs.values())
        return values[0] ** 2
    if figure == 'trapezoid':
        values = list(kwargs.values())
        res = (0.5 * (values[0] + values[1]) * values[2])
        return res
    if figure == 'circle':
        values = list(kwargs.values())
        return math.pi * values[0] ** 2


print(square('rhombus', a1=10, a2=8))
print(square('square', a=5))
print(square('trapezoid', a=12, b=3, h=6))
print(square('circle', r=18))
