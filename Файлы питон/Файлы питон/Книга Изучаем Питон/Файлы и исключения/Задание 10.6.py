while True:
    first_number = input('Enter the first number')
    if first_number == 'q':
         break
    second_number = input('Enter the second number')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ValueError:
        print('You cant devide int by str')
    else:
        print(answer)


