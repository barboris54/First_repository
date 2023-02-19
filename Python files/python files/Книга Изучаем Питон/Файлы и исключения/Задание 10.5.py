def devide_numbers():
    first_number = input('Enter the first number')
    second_number = input('Enter the second number')
    try:
        answer = int(first_number) / int(second_number)
    except ValueError:
        return print('You cant devide int by str')
    else:
        return print(answer)


devide_numbers()
