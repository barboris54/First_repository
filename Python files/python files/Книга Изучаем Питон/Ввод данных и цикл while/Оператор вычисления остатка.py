# При работе с числовыми данными может пригодиться оператор вычисления остатка (%), который делит одно число на другое и возвращает остаток:

print(5 % 3)  # = 2

5 % 4  # = 1

#  Например, этот факт может использоваться для проверки четности или
# нечетности числа:

number = int(input('Tell me your number and I will say its even or odd'))
if number % 2 == 0:
    print('This number is even')
else:
    print('This number is odd')