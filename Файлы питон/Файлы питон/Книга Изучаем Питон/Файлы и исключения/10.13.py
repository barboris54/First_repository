import json

def get_stored_name():
    """Получает хранимое имя пользователя"""
    filename = 'username_1.json'

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input('Enter your name').strip()
    filename = 'username_1.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Приветствует пользователя по имени"""

    print(f'Are you sure your name {get_stored_name()} is corretc ?')
    answer = input('y/n')
    if answer.strip() == 'y':
        username = get_stored_name()
        if username:
            print(f'Welcome back, {username}')
    else:
        username = get_new_username()
        print(f'We will remember you {username}')


greet_user()