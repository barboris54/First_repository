# d1 = {1: 10, 2: 20}
# d2 = {3: 30, 4: 40}
# d3 = {5: 50, 6: 60}
# d1.update(d2)
# d1.update(d3)
# print(d1)


# Задание 2

# dictionary = {
#     'emp1': {
#         'name': 'John',
#         'salary': 7500
#     },
#     'emp2': {
#         'name': 'Emma',
#         'salary': 8500
#     },
#     'emp3': {
#         'name': 'Brad',
#         'salary': 6500
#     }
# }
# print(dictionary['emp3'])
# for key, value in dictionary.items():
#     print(key)
#     for key1,value1 in value.items():
#         dictionary['emp3']['salary'] = 8500
#         print(f'{key1}:{value1}')

# Задание 3

students = int(input('Введите количтесво студентов: '))
dtc = {}
for i in range(students + 1):
    name = input('Введите имя студента: ')
    mark = int(input('Балл студента: '))
    dtc[name] = mark

for key, value in dtc.items():
    print(f'{students}-й студент :{key}\nБалл:{value}')

middle =  sum(dtc.values())// students
print('Средний балл - ', middle,'студенты с баллом выше среднего:')



for key,value in dtc.items():
    if dtc[key] > middle:
        print(key)

