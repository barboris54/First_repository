# Проблему можно решить при помощи функции int(), интерпретирующей строку
# как числовое значение. Функция int() преобразует строковое представление числа
# в само число

age = int(input('How old are you:'))
age >= 18

# или так

age_1 = input('How old are you ?')
age_1 = int(age_1)
if age_1 >= 18:
    print('you can vote')
else:
    print('you are too young to vote')


