# en = ['red','green','blue']
# j = 1
# for i in en:
#     print(j,'-',i)
#     j += 1
#
# en = ['red','green','blue']
# for j,i in enumerate(en,1):
#     print(j,'-',i)

# def func(*args):
#     return args
#
# print(func(1,2,3,4,5,6))

# def to_dict(*args):
#     return {i: i for i in args}
#
# print(to_dict(1,2,3,4))
# print(to_dict('gray',(2,17),3.11,-4))

# def func(*args):
#     lst = []
#     middle = sum(args) / len(args)
#     print(middle)
#     for i in args:
#         if i < middle:
#             lst.append(i)
#     return lst
#
# print(func(1,2,3,4,5,6,7,8,9))

# def func(a,*args):
#     return a, args
#
# print(func(1))
# print(func(1,2,3,'abc'))
#
# def print_scores(stud, *scores):
#     print('Student name:' , stud)
#     for score in scores:
#         print(score, end=' ')
#     print()
#
# print_scores('Jonatan',100,95,88,92,99)
# print_scores('Rick',88,95,72)

# def func(*args):
#     res = []
#     for i in args:
#         res.append(str(i)[::-1])
#     return res
#
# print(func(12,2345,323,4456,5687,62,734,81,93))

# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
# 
# def func(*args,only_odd = False):
#     res = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2):
#             res.append(reverse_num(i))
#     return res
# 
# print(func(12,2345,323,4456,5687,62,734,81,93))
# print(func(12,2345,323,4456,5687,62,734,81,93, only_odd = True))

# def info(**data):
#     for k,v in data.items():
#         print(k,'->',v)
#     print()
#
#
# info(first_name='Irina', last_name='Petrova', age=22, phone=1234567890)
# info(first_name='Igor', last_name='Ivanov', age=36,email='igoriv@gmail.com' ,phone=345435233)

# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eye_color='grey')
# print(my_dict)

# def func(*args):
#     print(args[0])
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
# func(1,2,3,4,5)
# func2(one=123,two=456)

# def func(a,*args,one=True,**kwargs):
#     return a,args,kwargs,one
#
# print(func(5,9,7,8,6,one = False, b=2, c=3, d=4))


