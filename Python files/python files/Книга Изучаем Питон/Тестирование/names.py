from function_name import get_formated_name
print('Prinnt your name and I will return it formated')
while True:
    first_name = input('Enter first name or press q to quit')
    if first_name == 'q':
        break
    last_name = input('Enter last name or press q to quit')
    if last_name == 'q':
        break
    formated_name = get_formated_name(first_name, last_name)
    print(formated_name)
