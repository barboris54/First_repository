import re

a = input('Введите дату в формате дд.мм.гггг :')
pattern = r'[1-3][0-9].[0-2][0-9].\d{4}'
print(re.findall(pattern, a))
