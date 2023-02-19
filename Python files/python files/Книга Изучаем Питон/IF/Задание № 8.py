list_of_users = ['tom','sam','william','jack','admin','boris']
for user in list_of_users:
    if user == 'admin':
        print(f'Hello, {user.title()}, would you like to see status report ?')
    else:
        print(f'Hello, {user.title()}, thank you for loggin again!')