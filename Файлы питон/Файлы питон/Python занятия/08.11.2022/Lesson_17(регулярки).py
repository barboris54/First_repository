# st = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(st)

# s = '-'
# seq = ('a','b','c')
# print(' '.join(seq))
# print(s.join(seq))
# a = list(map(int,input().split()))
# print(a)

# s = input('ФИО: ').split()
# print(f'{s[0]} {s[1][0]}. {s[2][0]}.')
# a = s.reverse()

# a = [1,2,3,4,5,6]
# b = list(reversed(a))
# print(b)
# _______________________________________________________________________________________________
import re

s = 'Я ищу совпадения в 2023. и я их найду в 2 счета.'
reg = r'\w'

# print(s.find(reg))
# print(re.findall(reg, s))  # Возвращает список всех совпадений ['я','я']
# print(re.findall('2023', s))
#
# print(re.search(reg, s))  # Ищет первое совпадения по шаблону
# print(re.search(reg, s).span())
# print(re.search(reg, s).group())
#
# print(re.split(reg, s, 1))
#
# print(re.sub(reg, '!', s, 1))
#
# s1 = 'Ели[-ели].'
# pattern = r'[A-я.-]'

print(re.findall(reg, s))
# print(re.findall(pattern, s1))

# s = 'Час в 24-часовои формоте от 00 до 23. 2021-06-15Т21:21:45. Минуты в диапозоне от 00 до 59.2121-06-15Т01:09.'
# reg = '[0-2][0-9]:[0-5][0-9]'
#
# print(re.findall(reg, s))
