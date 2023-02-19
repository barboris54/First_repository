# a = {'Tom','Bob','Alice'}
# a.add('Ann')
# print(a)
# a.remove('Tom')
# print(a)
# a.discard('Tom')

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}

# c = a.union(b)
# print(c)
# a.update(b)
# print(a)
# c = a & b
# print(c)
# c = a - b
# print(c)
# c = a ^ b
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# s1 = 'Python'
# s2 = 'Programming langueage'
# st = set(s1) - set(s2)
#
# print(st)
#
# drawind = {'Marina','Jenya','Sveta'}
# music = {'Kostya','Jenya','Ilya'}
#
# only = drawind ^ music
# print('Одно хобби:',only)
#
# both = drawind & music
# print('Два хобби: ', both)
#
# drawind = drawind - both
# print(drawind)

# s = frozenset([1,2,3,4,5,4])
# print(s)

# Словари
# s = ['one','two',]
# print(s[0])
# d = {1: 'one', 2 : 'two'}
# print(d[1])

# d1 = dict(one=1, two=2)
# print(d1)
# print(type(d1))

# a = [
#     ('igor@gmail.com','igor'),
#     ('irina@gmail.com','irina'),
#     ('anna@gmail.com','anna'),
# ]
# d = dict(a)
# print(d)

# d = {a: a**2 for a in range(1,7)}
# print(d)
# print(d[2])
# d[2] = 15
# print(d)
# d[6] = 4 ** 2
# print(d)

# d = {0:'text', 'one' : 45, (1,2.3): "кортеж"}
# print(d)
# key = (1,2.3)
# print('one' in d)
# # print(d.keys())
# try:
#     del d[key]
# except KeyError:
#     print('Элемента с таким ключом нет')
# print(d)

# d= {'x1':3, 'x2': 7, 'x3':5, 'x4':-1}
# pro = 1
# for i in d:
#     pro *=d[i]
# print(pro)

# d = {}
# d[1] = input('-> ')
# d[2] = input('-> ')
# d[3] = input('-> ')
# d[4] = input('-> ')
# print(d)

# d = {a: input("->") for a in range(1,5)}
# print(d)
# dl = int(input('какой элемент исключить '))
# del(d[dl])
# print(d)
#
# capitals = {}
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals['Испания'] = 'Мадрид'
#
# countries = ['Россия','Италия','Франция','Испания']
#
# for counutry in countries:
#     if counutry in capitals:
#         print(capitals[counutry])
#     else:
#         print('Такой страны нет в базе')
#
# goods = {
#     1:['Core-i3',9,4500],
#     2:['Core-i5',3,8500],
#     3:['AMD FX-6300',9,3700],
#     4:['Pentium G3220',9,2100],
#     5:['Core-i5-3450',9,4600]
# }
# for i in goods:
#     print(i, ') ', goods[i][0]," - ",goods[i][1],' по ', goods[i][2],'руб', sep='')
#
# while True:
#     num = int(input('№ '))
#     if num == 0:
#         break
#     else:
#         count = int(input('Количество '))
#         goods[num][1] = count
#
# for i in goods:
#     print(i, ') ', goods[i][0]," - ",goods[i][1],' по ', goods[i][2],'руб', sep='')

# d = {1: 't', 2: 'w'}
# # values = d.get(3,'No')
# # print(values)
# # a = d.popitem()
# # print(a)
# # item = d.setdefault('e',5)
# # print(d)
# d.update([('r', 7), ('q',9)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b':4, 'c':5}
# c = x.copy()
# c.update(y)
# print(c)

# d1 = {'name': 'Kelly', 'age':25 , 'salary': 8000, 'city': 'New York'}
# d2 = {}
# name = d1.pop('name')
# salary = d1.pop('salary')
# print(d1)
# d2['name'] = name
# d2['salary'] = salary
# print(d2)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three',
#     },
#     'seocnd': {
#         4: 'four',
#         5: 'five'
#     }
# }
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t',y,":",a[x][y],sep='')

# d = {'one': 1, 'two': 2, 'three': 3, 'четыре': 4}
# a = {key:value for key,value in d.items() if value <=2}
#
# print(a)

# value = int(input('->'))
# lt = [1,2,3,4,5]
# a = {i: value for i in lt}
# print(a)

# figures = {1:'Rectangle',2:'Triangle', 3:'Cirle'}
# value = list(figures.items())
# print(value)

# a = ['one',1,2,3,'two',10,20,'three',15,36,60,'four',-20]
# d = {}
# key = ''
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         key = i
#     else:
#         d[key].append(i)
# print(d)

#                           zip()

# d = list(zip([1,2,3], ['one','two','three']))
# print(d)
# c = dict(zip([1,2,3], ['one','two','three']))
# print(c)
#
#
# a = [12,1,2]
# b= ['ad','as','sd']
# f = {k: v for k,v in zip(a,b)}
# print(f)

# a = {'name':'Igor', 'last_name':'Doe', 'job': 'Consultant'}
# b = {'name':'Irina', 'last_name':'Smith', 'job': 'Manager'}
#
# for (k1, v1),  (k2, v2) in zip(a.items(),b.items()):
#     print(k1,'->', v1)
#     print(k2,'->', v2)

# month = ['January','Fabruary','March']
# total_sales = [52000.00,51000.00,48000.00]
# prod_cost = [46800.00,45900.00,43200.00]
#
# for sales, cost, m in zip(total_sales,prod_cost, month):
#     res = sales - cost
#     print('Общая прибыль в',m, '=', res)

# one = {'apple': 0.4, 'orange':0.35}
# two = {'peper': 0.2, 'onion':0.55}
# print({**one,**two})
#
# for k,v in {**one,**two}.items():
#     print(k,'->', v)