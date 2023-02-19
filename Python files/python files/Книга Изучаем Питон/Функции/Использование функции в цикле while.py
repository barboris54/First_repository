def get_formeted_name(first_name,last_name):
    full_name = (f'{first_name} {last_name}')
    return full_name.title()
while True:
    print('\nTell me your name')
    print("print 'q' at any time to quit")
    f_name = input('First name').strip()
    if f_name == 'q':
        break
    l_name = input('Last name').strip()
    if l_name == 'q':
        break

    formated_name = get_formeted_name(f_name,l_name)
    print(formated_name)