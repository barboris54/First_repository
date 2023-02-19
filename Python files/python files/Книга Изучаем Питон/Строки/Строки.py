name = 'ada lovelace'
print(name.title())

# Метод title() преобразует первый символ каждого слова в строке к верхнему регистру

name_1 = 'Ada Lovelace'
(name_1.upper())  # метод upper преобразует все символы в строке к верхнему регистру ADA LOVELACE
(name_1.lower())  # метод lower преобразует все символы в строке к нижнему регистру ada lovelace

first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}' # Такие строки называются f-строками.
                                              # Буква f происходит от слова «format», потjму что Python форматирует строку,
                                              # заменяя имена переменных в фигурных скобках их значениями
print(full_name)
