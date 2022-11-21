# Задание № 1

number = int(input('введите пятизначное число '))
if len(str(number)) == 5:
    a = number // 10000
    b = number % 10
    c = (number % 100) // 10
    d = (number % 1000) // 100
    e = (number % 10000) // 1000
    print(
        f'Произведение цифр числа {number}: {a * b * c * d * e}\nСреднее арифметическое: {(a + b + c + d + e) / len(str(number))}')
else:
    print('Введеное число не пятизначное')

# Задание № 2

number2 = int(input('Введите целое число '))
if number2 % 2 == 0:
    print(f'Число {number2} - четное\n\n')
else:
    print(f'Число {number2} - нечетное\n\n')

# Задание № 3

print("Выберите оператор\n"
      "1. 'r' - применяет унитарный минус к операнду\n"
      "2. '+' - сложение\n"
      "3. '-' - вычетание\n"
      "4. '/' - деление\n"
      "5. '*' - умножение\n"
      "6. '%' - остаток от деления\n"
      "7. '>' - большее из двух чисел\n"
      "8. '<' - минимальное из двух чисел\n")
inp1 = int(input('Введите номер оператора из предложенных '))
inp2 = int(input('Введите первое число '))
if inp1 == 1:
    print(f'-{inp2}')
else:
    inpt3 = int(input('Введите второе число '))
    if inp1 == 2:
        print(f'Cумма чисел: {inp2 + inpt3}')
    if inp1 == 3:
        print(f'Разность чисел: {inp2 - inpt3}')
    if inp1 == 4:
        if inpt3 == 0:
            print('Нельзя делить на 0')
        else:
            print(f'Частное чисел: {inp2 / inpt3}')
    if inp1 == 5:
        print(f'Произведение чисел: {inp2 * inpt3}')
    if inp1 == 6:
        if inpt3 == 0:
            print('Нельзя делить на 0')
        else:
            print(f'Остаток от деления чисел: {inp2 % inpt3}')
    if inp1 == 7:
        if inp2 > inpt3:
            print(f'Большее число {inp2}')
        else:
            print(f'Большее число {inpt3}')
    if inp1 == 8:
        if inp2 < inpt3:
            print(f'Меньшее число {inp2}')
        else:
            print(f'Меньшее число {inpt3}')

# Задача № 4

kop = int(input('Введите число от 1 до 99 '))
if len(str(kop)) == 1:
    if kop == 1:
        print(f'{kop} копейка')
    elif (kop == 2) or (kop == 3) or (kop == 4):
        print(f'{kop} копейки')
    else:
        print(f'{kop} копеек')
else:
    if 10 <= kop <= 20:
        print(f'{kop} копеек')
    else:
        if kop % 10 == 1:
            print(f'{kop} копейка')
        elif (kop % 10 == 2) or (kop % 10 == 3) or (kop % 10 == 4):
            print(f'{kop} копейки')
        else:
            print(f'{kop} копеек')