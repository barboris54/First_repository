def greet_users(names):
    """ Greatings all members """
    for name in names:
        msg = print(f'Hello, {name.title()}')

user_names = ['hanna','ty','margot']
greet_users(user_names)