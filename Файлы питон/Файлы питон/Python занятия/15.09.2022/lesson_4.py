# n = input('введите целое число ')
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print('число не целое !')
#         n = input('введите целое число ')
#
#
# if n % 2 == 0:
#     print('четное')
# else:
#     print('нечетное')

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")

# while True:
#     n = int(input('введите положительное число '))
#     if n < 0:
#         n = int(input('введите положительное число '))
#     else:
#         break
# sum = 1
# while True:
#     n = int(input('введите число '))
#     if n == 0:
#         break
#     sum *= n
#
# print(sum)

# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print('Цикл окончен, i =',i)

# i = 1
# while i < 9:
#     print()
#     i += 1
#     j = 1
#     while j < 10:
#         print(j, '*',i,'=',i*j, end='\t\t')
#         j += 1

# i = 1
# while i <= 5:
#     j=0
#     while j<20:
#         if i%2!=0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j+=1
#     print()
#     i+=1

# for i in range(9,0,-1):
#     print(i,end=' ')

# a = int(input('введите целое число '))
# for i in range(1,a):
#     if a % i == 0:
#         print(i)
#
# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")
#
# for i in range(3):
#     print(i)
# else:
#     print('done')

# n = int(input('введите длину '))
# m = int(input('введите высоту '))
# for i in range(m):
#     for j in range(1,n):
#         if i == 1 or i ==n:
#             print('*',end='')
#     print()

a = int(input("высота прямоугольника"))
b = int(input("Ширина прямоугольника"))
for i in range(a):
    print()
    for j in range(b):
        if 0 < i < a - 1 and 0 < j < b - 1:
            print(" ", end="")
        else:
            print("*", end="")