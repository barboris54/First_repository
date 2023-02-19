# Задание 1

# print((lambda a, b, c: a * b * c)(2, 5, 5))

# Задание 2
#
# lst = [{'name': 'Jannifer', 'final': 95},
#        {'name': 'David', 'final': 92},
#        {'name': 'Nikolas', 'final': 98}]
#
# res = sorted(lst, key=lambda i: i['name'], )
# res1 = sorted(lst, key=lambda i: i['final'], reverse=True)
# print(res)
# print(res1)

# Задание 3
#
# lst = [{'name': 'Jannifer', 'final': 95},
#        {'name': 'David', 'final': 92},
#        {'name': 'Nikolas', 'final': 98}]
#
# max1 = sorted(lst, key=lambda i: i['final'],reverse=True)[0]['final']
# print(max1)
# min1 = sorted(lst, key=lambda i: i['final'],reverse=True)[-1]['final']
# print(min1)

# Задание 4

nums = [3, 5, 7, 3, 9, 5, 7, 2]

square = list(map(lambda x: x**2, nums))
cube = list(map(lambda x: x**3, nums))
print(square)
print(cube)