# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)(3, 5))

# print((lambda x,y: (x**2) + (y**2))(2,5))

# func1 = lambda *args: args
# print(func1(1, 2, 3, 4, 5))

# c = (lambda x: x * 2,
#     lambda x: x* 3,
#     lambda x: x* 4)
#
# for t in c:
#     print(t('abc'))

# def inc(n):
#     return lambda x: x + n
#
#
# f = inc(42)
# print(f(3))
#
# inc2 = (lambda n: (lambda x: x + n))
# print(inc2(42)(3))

# print(lambda n: (lambda x: x + n)(42)(3))


# sum = (lambda a,b,c: a + b + c)
# print(sum(1,2,3))
#
# sum = (lambda a : (lambda b: (lambda c: a + b + c)))
# print(sum(1)(2)(3))


# !!!!!!


# d = {'b': 15,'a': 10,  'c': CAR}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# dict1 = dict(lst)
# print(dict1)

# players = [
#      {'name': 'Антон', 'last_name': 'Бирюков', 'raiting': 9},
#      {'name': 'Алексей', 'last_name': 'Бодня', 'raiting': 10},
#      {'name': 'Федор', 'last_name': 'Сидоров', 'raiting': 4},
#      {'name': 'Михаил', 'last_name': 'Семенов', 'raiting': 6}]
#
# res = sorted(players, key=lambda x: x['last_name'])
# print(res)
# res1 = sorted(players, key=lambda x: x['raiting'])
# print(res1)

# a = [(lambda x,y,: x+y), (lambda x,y: x-y),(lambda x,y : x * y),(lambda x,y : x//y)]
# b = a[2](12,5)
# print(b)

# a = {'one': lambda x: x-1, 'two': lambda x: abs(x) -1, 'three': lambda x: x}
# b = [-3,10,0,2]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: (lambda : print('Понедельник')),
#     2: (lambda : print('Вторник')),
#     3: (lambda : print('Среда')),
#     4: (lambda : print('Четверг')),
#     5: (lambda : print('Пятница')),
#     6: (lambda : print('Суббота')),
#     7: (lambda : print('Воскресенье')),
# }
# d[4]()

# maximum = (lambda a,b : a if a > b else b)
# print(maximum(15,23))

# !!!!

# minimum = (lambda a,b,c : a if (a < b and a < c) else (b if b < a and b < c else c))
# print(minimum(11,12,1))

# Функция map()

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))
# print(list(map(lambda t: t * 2, lst)))

# t = 2.88 , -1.175, 100.88
#
# print(tuple(map(lambda x: int(x), t)))
#
# a = [2.88 , -1.175, 100.88]
# print(list(map(float, a)))

# areas = [3.425435666,5.546546754654,56.435353535]
# print(list(map(round,areas,range(1,4))))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5,]
#
# lst = list(map(lambda x, y: (x, y), st, num))
# print(lst)
# tp = dict(lst)
# print(tp)

l1 = [1, 2, 3]
l2 = [4, 5, 6]

res = list(map(lambda x, y: x + y, l1, l2))
print(res)
