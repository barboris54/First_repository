import re

#
# s1 = 'Дата рождения: 05-03-1987'
# print('Дата рождения:', re.sub(r'-','.',s1))
# print('Дата рождения:', re.sub(r'-?#.*', '.', s1)[:-1])

# s1 = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831'
# pattern = r'\w+\s*+=\s*[^;]+'
# print(re.findall(pattern, s1))

# s = '12 сентября 2021 года'
# reg1 = r'\d{2,4}'
# print(re.findall(reg1, s))

# s = '7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# pattern = r'\+?7\d{10}'
# print(re.findall(pattern, s))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))
# print(re.findall(r'[а-я]', 'Я я', re.IGNORECASE))
#
# text = """
# one
# two
# """
# print(re.findall(r'one$',text))
# print(re.findall(r'one$',text, re.MULTILINE))