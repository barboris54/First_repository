print('Give me two numbers and I will devide them')
print('Enter q to exit')
while True:
    first_number = (input('\nGive me the first number'))
    if first_number.strip() == 'q':
        break
    second_number = (input('\nGive me a second number'))
    if second_number.strip() == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You cant device by zero')
    else:
        print(answer)
