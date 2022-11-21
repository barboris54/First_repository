import re

# print(re.findall("""[A-z.-]+
# @
# [a-z_.-]+
# """, 'test@mail.ru',re.VERBOSE))

# text = 'hello word'
# print(re.findall(r'\w+',text, re.DEBUG))

# text = """Python
# python
# PYTHON"""
# reg = '(?im)^python'
# print(re.findall(reg, text, ))  # flags=re.IGNORECASE | re.MULTILINE

# s = '123456@i.ru, 123_456@ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
# reg = r'[\w.-]+@[\w.]+[^., ]'
# print(re.findall(reg, s))

# text = '<body>Пример жадного соответствия регулярных выражений</body>'
# print(re.findall('<.+>',text)) # жадное вырожение берет максимум символов
# print(re.findall('<.+?>',text)) # *? или +? ленивое вырожение берет минимум сиволов

# t = '2324 786 22 4569'
# reg = r'\d{1,3}'
# reg1 = r'\d{1,3}?'
# print(re.findall(reg,t))
# print(re.findall(reg1,t))

# s = '<p>изображение<img src= bg.jpg> - фон страницы</p>'
# reg = r'<img\s+[^>]*?src\s*=\s*[^>]+>'
# print(re.findall(reg, s))

# text = 'Python (в русском языке встречается название питон[16] или пайтон[17]) - высокоуровневый язык прогрмаммирования[18]'
# print(re.findall(r'\[\d+]',text))

# s = 'Петр и Ольга отлично учатся !'
# reg = 'Петр|Виталий|Ольга'
# print(re.findall(reg,s))

# s = 'int = 4, float = 4.0, double = 8.0f'
# # reg = r'\w+\s*=\s*[\d.\w]+'
# reg = r'(?:int|float)\s*=\s*\d+[.\w+]*'
# print(re.findall(reg, s))

# () - группирующая скобка
# (?:) - группирующая скобка, не сохранающая

# s = '127.0.0.1'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s))
#
# s = 'Word2016, PS6, AI5'
# reg = r'[A-z]+\d*'
# print(re.findall(reg, s))

s = '5 + 7*2 - 4'
# reg = r'\s*[+*-]\s*'
reg = r'\s*(?:[+*-])\s*'
print(re.split(reg, s))
