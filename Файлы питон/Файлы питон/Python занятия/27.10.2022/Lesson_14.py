# Filter(func, iterable)
import random


# t = ('abcd','abc', 'cdefg','def','ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
#
# b = [66,90,68,59,74,39]
# res = list(filter(lambda s: s > 60,b))
# print(res)

# lst = [random.randint(1,100) for _ in range(10)]
# print(lst)
# res = list(filter(lambda s: 10 <= s <= 20, lst))
# print(res)

# lst = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda s: s % 15 == 0, lst))
# print(res)

# Декораторы

# def hello():
#     return 'Hello I am func "hello"'
#
# def super_func(func):
#     print('Hello I am func "super_hello"')
#     print(func())
#
# super_func(hello)

# def my_decarator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('code after')
#     return wrap
#
# def func_test():
#     print('Hello')
#
# test = my_decarator(func_test)
# test()

# def my_decarator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('code after')
#     return wrap
#
# @my_decarator
# def func_test():
#     print('Hello')
#
# func_test()

# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#     return wrap
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#     return wrap
#
# @italic
# @bold
# def hello():
#     return 'text'
#
# print(hello())

# def count_hello(fn):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         fn()
#         print(f'Вызов функции {count}')
#
#     return inner
#
# @count_hello
# def hello():
#     print('hello')
#
# hello()
# hello()
# hello()

def stars(fn):
    def wrap(*args, **kwargs):
        print('*' * 10)
        fn(*args,**kwargs)
        print('args', args)
        print('kwargs', kwargs)
        print('*' * 10)

    return wrap


@stars
def print_full_name(a,b,c,study='Python'):
    print(a,b,c,'изучают', study, end='\n\n')


print_full_name('Ирина','Борис','Светалана', study='JavaScript')
print_full_name('Владимир','Екатерина','Виктор')


# ______________________________________________________________________________________

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(f'{args1}: {x} {args2} {y} =', end=' ')
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor('Сумма:', '+')
# def summa(a, b):
#     print(a + b)

#
# @decor('Разность', '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# __________________________________________________________________________________________

# def multiply(x):
#     def inner1(fn):
#         def inner2(a):
#             print(a * x)
#             fn(a)
#
#         return inner2
#
#     return inner1
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# return_num(5)

def typed(*args,**kwargs):
    def wrap(fn):
        def inner(*f_args,**f_kwargs):
            for i in range(len(args)):
                if type(f_args[i]) != args[i]:
                    raise TypeError('Некорректный тип данных')
            for k in kwargs:
                if type(f_kwargs[k]) != kwargs[k]:
                    raise TypeError('Некорректный тип данных')
            return fn(*f_args,**f_kwargs)

        return inner
    return wrap
@typed(int,int,int)
def typed_fn(x, y, z):
    return x * y * z

@typed(str,str,str)
def typed_fn2(x, y, z):
    return x + y + z
@typed(str,str,z=int)
def typed_fn3(x, y, z='hello'):
    return (x + y) * z

print(typed_fn(3,4,5))
# print(typed_fn(3,4,'Dog'))
print(typed_fn2('hello', 'World', '!'))
print(typed_fn3('hello', 'World', z=5))
#print(typed_fn3('hello', 'World', z="!!!"))