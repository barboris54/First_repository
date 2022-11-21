# n = int(input('Введите начало диапазона (включительно): '))
# m = int(input('Введите конец диапазона (включительно): '))
# start = n if n < m else m
# finish = m if n < m else n
# count = 0
# while start <= finish:
#     count += start if start % 2 != 0 else 0
#     start += 1
# print('Сумма целых нечетных чисел:', count)


# a = [letter * 2 for letter in 'Hello']
# print(a)

# num = [i for i in range(30) if i % 2 ==0]
# print(num)
# num = [8,3,[1,2,3],'one']
# print(num[-1])
# print(num[-2][-1])

# print(len([i for i in range(30) if i % 2 ==0]))

# b = list(('hello', 'word'))
# print(b)

# s = [5]*6
# print(s)

# n = list(range(2,10,2))
# print(n)
# n2 = [2, 4, 6, 8]
# print(n2)
# if n in n2:
#     print('списки равны')
# else:
#     print('списки разные')

# a = [0] * int(input('Введите число '))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input('Введите число '))
#
# print(a)

# a = [input('Введите элемент ') for i in range(int(input('кол-во элементов ')))]
# print(a)

# a = [1,2,3,4,5,6]
# for i in range(len(a)):
#     print(a[i])

# count = 0
# lst = [int(input('=> ')) for _ in range(int(input('Введите количетсов элементов ' )))]
#
# for i in lst:
#     if i < 0:
#         count += i
# print(f'сумма отрицательных элементов {count}')

# count = 0
# sum = 0
# n = list(range(21, 41))
# for i in n:
#     count += 1 if i % 2 == 0 else 0
#     sum += i if i % 2 else 0
# print(count, sum)


# n = 5
# zero_elem = 0
# sum1 = 0
# lst = [int(input('->')) for _ in range(n)]
# for i in lst:
#     if i == 0:
#         zero_elem += 1
#     sum1 += i
# print('Среднее арифметическое - ', sum1 / (n - zero_elem))

a = [int(input("->")) for i in range(int(input("Количество элементов: ")))]
for i in range(len(a)):
    if i % 2 == 0:
        print(a[i], end=' ')
