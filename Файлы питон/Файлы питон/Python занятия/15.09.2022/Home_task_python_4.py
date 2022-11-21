# try:
#     n = int(input('Введите начало диапозона '))
#     m = int(input('Введите конец диапазона '))
#     if n > m:
#         n, m = m, n
#     for i in range(n,m+1):
#             if i % 2 != 0:
#                 print(i, end=' ')
# except ValueError:
#     print('вы ввели не целое число !')


# print('Угадайте загаданное число. Если вам надоело играть введите 0 для выхода.')
# n = 51
# count = 0
# while True:
#     try:
#         m = int(input('Введите число от 1 до 99 '))
#         if m < n and m != 0:
#             print('Загаданное число больше')
#             count += 1
#         if m > n and m != 0:
#             print('Загаданое число меньше')
#             count += 1
#         if m == n:
#             print('Вы угадали число ! Поздравляем !')
#             count += 1
#             break
#         if m == 0:
#             break
#     except ValueError:
#         print('вы ввели не целое число !')
# print(f'Вы потратили {count} попыток')


n = int(input("введите размер поля "))
m = int(input('Введите количество символов '))

for i in range(n):
    for j in range(n):
        if i % 2 != 0:
            if j % 2 == 0:
                print(' ', end=' ')
            else:
                print('*', end='')

        else:
            if j % 2 != 0:
                print(' ', end=' ')
            else:
                print('*', end='')

    print()
