# операции с множествами
# 1.Нахождение длинны множества с помошью len
a = {1,2,3,4,5}

print(len(a))

# 2. Проверка на принадлежность элемнта к множеству
b={1,2,3,4,5,6}

print (4 in b, 8  not in b)

# 3. нахождение пересeчений множеств с помошью & или метода intersection
c = {1,2,5,12,15}

print (a & c)

# или

print (a.intersection(c))

# 4. объединение множеств (без дублей) выполняеться с помошью | или метода union

print (a | c)

# или

print (a.union(c))

# 5. множества можно вычетать друг из друга, при этом будут удаляться все повторяющиеся элементы

print (b-a)
print (a-b)

#  6. Симметричная разность выполняется с помошью ^ - результатом этой операции будут все элемнты за исключением тех которые принадлежат к этим множествам

print (a^c)