import random

# def random_tupple(n,m):
#     tpl = (tuple(random.randint(n,m) for _ in range(10)))
#     return tpl
# a = int(input('->'))
# b = int(input('->'))
# first = (random_tupple(a,b))
# second = (random_tupple(a,b))
# new_tupple = first + second
# print(first)
# print(second)
# print(new_tupple)
# print('количество 0:',new_tupple.count(0))

# def set_elements(lst):
#     tpl = set(lst)
#     return tpl
# a = set_elements([1,2,3,4,4,1,6,78,23,3])
# tpl = tuple(a)
# print(tpl[::-1])

# Распаковка кортежа
# t = (1,2,3,)
# x,y,z = t
# print(x,y,z)

# countries = (
#     ('ger',80, (('Ber',232),('gam',12313))),
#     ('fra', 90,(('par',123),('mar',712153)))
# )
#
# for i in countries:
#     countyName, population, cities = i
#     print(countyName, population )
#     for city in cities:
#         city_name, cityPop = city
#         print(city_name,cityPop)

# def to_set(elem):
#     st = set(elem)
#     return st, len(st)
#
# print(to_set('я обычная строка'))
# print(to_set([4,5,4,6,2,9,11,3,4,2]))

r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if[1] == 'c'}
print(a)
