# n = int(input('Введите колчиство ворон: '))
# if 0<= n <=9:
#     print('на ветке ',end='')
#     if n == 1:
#         print(n,'ворона')
#     if 2<= n <=4:
#         print(n, 'вороны')
#     if 5 <= n <= 9 or n == 0:
#         print(n,'ворон')
# else:
#     print('Ошибка ввода данных')

# a = int(input('ввндите число от 1 до 99: '))
# kop = a
# if 11 <= kop <=14:
#     print(a,'копеек')
# else:
#     kop = kop % 10
#     if kop == 1:
#         print(a,'копейка')
#     elif kop == 2 or kop == 3 or kop == 4:
#         print(a,'копейки')
#     else:
#         print(a,'копеек')

                                # ТЕРНАРНОЕ ВЫРОЖЕНИЕ



# a, b = 30,20
# minim = a  if a < b else b
# print(minim)

# a, b = 50,60
# print('a == b' if a == b else 'a > b' if a > b else 'b > a')

# a = int(input('введите делимое '))
# b = int(input('введите делитель '))
# print('На ноль делить нелmзя' if b == 0 else a / b)


                                            # Исключения

# try:
#     n = int(input('Введите целое число'))
#     print(n*2)
# except ValueError:
#     print('Что-то пошло не так')
# print('Текст далее')

# try:
#     n = int(input('Введите делимое'))
#     m = int(input('Введите делитель'))
#     print(n / m)
# except ValueError:
#     print('Нельзя вводить строки')
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")
# else: # когда в блоке try не возникло исключений
#     print('Все нормально. Вы ввели числа', n,'и', m)
# finally: # выполняется в любом случае
#     print('Конец программы')

# n = input('Введите первое число ')
# m = input('Введите второе число ')
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#    n = str(n)
# finally:
#     print(n + m)

# i = 0
# while i < 5:
#     print('i = ',i)
#     i += 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1
n = int(input(' '))
i = 0
while i < n:
    print('*', end='')
    i += 1