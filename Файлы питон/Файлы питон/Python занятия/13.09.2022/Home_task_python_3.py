try:
    num1 = int(input('введите начало диапозона: '))
    num2 = int(input('введите конец диапазона: '))
    sum = 0
    if num1 < num2:
        i = num1
        while i < num2 + 1:
            if i % 2 != 0:
                sum += i
                i += 1
            else:
                i += 1
    else:
        i = num2
        while i < num1 + 1:
            if i % 2 != 0:
                sum += i
                i += 1
            else:
                i += 1
    print(sum)
except ValueError:
    print('вы ввели не целое число !')

