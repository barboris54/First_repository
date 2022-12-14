# В языке Python проверка равенства выполняется с учетом регистра. Например, два
# значения с разным регистром символов равными не считаются. Audi и audi не равны

car = 'audi'
print (car == 'Audi') # False

# Если регистр символов важен, такое поведение приносит пользу. Но если проверка
# должна выполняться на уровне символов без учета регистра, преобразуйте значение
# переменной к нижнему регистру перед выполнением сравнения:

car_1 = 'Audi'
print(car_1.lower() == 'audi') # True
