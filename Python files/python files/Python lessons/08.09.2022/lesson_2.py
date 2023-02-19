#name = 'Boris'
#age = 28
#print('My name is',name, "I am ", age, 'years old', sep="---", end='\n\n')

#num = int(input('Введите число '))
#num1 = int(input('введите степень числа '))
#print(num**num1)

#num1 = int(input('введите число '))
#num2 = int(input('введите число '))
#num3 = int(input('введите число '))
#num4 = int(input('введите число '))

#a = (num1 + num2) / (num3 + num4)
#print(a)

a = int(input('Введите значение стороны '))
b = int(input('Введите значение стороны '))
c = int(input('Введите значение стороны '))

if (a == c == b):
    print('Треугольник равносторонний')
elif (a == b) or (b == c) or (a == c):
    print('Треугольник равнобедренный')
else:
    print('Треугольник разносторонний')



