# def outer(who):
#     def inner():
#         print('hello',who)
#     inner()
#
# outer('world')

# def func1():
#     a = 1
#
#     def func2(b):
#         a = 4
#         print('summa ',a + b)
#     print('a = ', a)
#     func2(4)
#
#
# func1()

# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     print('global:', x)
#
#     def inner():
#         nonlocal a
#         a = 35
#         print('nonlocal:', a)
#
#     inner()
#     t = a
# fn()
# z = x + t
# print(z)
#
# def fn():
#     x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2', x)
#
#     fn2()
#     print('fn1', x)
#
#
# fn()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#
#     return [a,b]
#
# res = outer(2,3,-1,4)
# print(res)

# def increment(number):
#     def inner():
#         return number + 1
#     return inner()
#
# print(increment(10))

# def outer(n):
#     def inner(x):
#         return n + x
#     return inner
#
#
# print(outer(5)(10))

# res = outer(5)
# print(res(10))
# print(res(2))
#
# res2 = outer(7)
# print(res2(5))

# def func1():
#     a = 1 # неизменяемый тип
#     b = 'line' # неизменяемый тип
#     c = [1,2,3] # изменяемый тип
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         b = b + 'new'
#         a = a + 1
#         return a,b,c
#
#     return func2
#
# func = func1()
# print(func())

#
# def func(city):
#     s = 0
#     def inner():
#         nonlocal s
#         s += 1
#         print(city,s)
#     return inner
#
# res1 = func('Moskow')
# res1()
# res1()
#
# res2 = func('Sochi')
# res2()
# res2()


# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Elise': 54,
#     'Fiona': 35,
# }
#
#
# def make_clssifier(lower, upper):
#     def classify_students(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return classify_students
#
#
# A = make_clssifier(80, 100)
# B = make_clssifier(70, 80)
# C = make_clssifier(50, 70)
# D = make_clssifier(0, 50)
# print(A(students))
# print(B(students))
# print(C(students))
# print(D(students))

def func(a, b):
    def add():
        return a + b

    def sub():
        return a - b

    def mul():
        return a * b

    def replace():
        pass

    replace.add = add
    replace.sub = sub
    replace.mul = mul
    return replace


obj1 = func(5, 2)
print(obj1.add())
print(obj1.sub())
print(obj1.mul())
