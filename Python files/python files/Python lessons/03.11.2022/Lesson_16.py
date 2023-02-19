# print(ord('a'))
#
# while True:
#     n = input('->')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break

# mystr = 'Test string for me'
# arr = [ord(i)for i in mystr]
# print(arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print(arr)
# arr += [x for x in [ord(x) for x in (input("->"))[:3]] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print(arr.count(arr[-1]) -1)
# arr.sort(reverse=True)
# print(arr)
# print(chr(97))
# print(chr(44))
# print(chr(3333))

# a = 122
# b = 97
#
# for i in range(b,a+1):
#     print(((chr(i))),end=' ')

# from random import randint
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
# def random_password():
#     random_length = randint(SHORTEST,LONGEST)
#     res = ''
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII,MAX_ASCII))
#         res += random_char
#     return res
#
# print('Ваш пароль', random_password())

# print(dir(str))

# s = 'hello, WORLD! I am learning Python'
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.swapcase()) # HELLO, world! i AM LEARNING pYTHON
# print(s.title())

# s = 'ab12c59p7dq'
# arr = []
# for i in '123456789':
#     if i in s:
#         arr.append(i)
# print(arr)
#
# s = 'asdashello, WORLD! I am learning Python'
# a = s.find('h')
# b = s.find('h', a+1)
# s = (s[:a] + s[b:])
# print(s)

print('abc123'.isalnum()) # определяет состиоит ли строка из цифр или букв

