# Задание № 1
# def multiply(a):
#     def inner(b):
#         return a*b
#     return inner
# res = multiply(2)
# print(res(15))
# print(res(20))
# res = multiply(3)
# print(res(15))
# print(res(20))

# Задание № 2
# Вариант 1
s = 0


# def square1(a, b, c):
#     def inner(x, y):
#         global s
#         s = x * y
#         return s
#
#     return 2 * (inner(a, c) + inner(c, b) + inner(a, b))
#
# print(square1(2,4,6))
# print(square1(5,8,2))
# print(square1(1,6,8))

# Вариант 2
# def square1(a, b, c):
#     s = 0
#     def inner(x, y):
#         nonlocal s
#         s = x * y
#         return s
#     return 2 * (inner(a, c) + inner(c, b) + inner(a, b))
#
# print(square1(2,4,6))
# print(square1(5,8,2))
# print(square1(1,6,8))

# Вариант 3

def square1(a, b, c):
    def inner(x, y):
        s = x * y
        return s
    return 2 * (inner(a, c) + inner(c, b) + inner(a, b))

print(square1(2,4,6))
print(square1(5,8,2))
print(square1(1,6,8))