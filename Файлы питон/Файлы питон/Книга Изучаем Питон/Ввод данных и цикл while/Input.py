# Как работает функция input()
# Функция input() приостанавливает выполнение программы и ожидает, пока
# пользователь введет некоторый текст. Получив ввод, Python сохраняет его в переменной, чтобы вам было удобнее работать с ним.
message = print(input('print me something and i will repeat it back to you:'))
print(message)

# или

name = input('please enter your name')
print(f'Hello {name.title()}')

# Иногда подсказка занимает более одной строки. Например, вы можете сообщить
# пользователю, для чего программа запрашивает данные. Текст подсказки можно
# сохранить в переменной и передать эту переменную функции input(): вы строите
# длинное приглашение из нескольких строк, а потом выполняете одну компактную
# команду input()

promt = 'If you say who who are, we can personalize the message you see'
promt += '\nWhat is your first name ?' #  оператор += объединяет текст, хранящийся в prompt, с новым фрагментом текста.

name_1 = input(promt)
print(f'Hello {name_1.title()}')