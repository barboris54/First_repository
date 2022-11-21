import json


# Часто возникает типичная ситуация: код работает, но вы понимаете, что его структуру можно усовершенствовать, разбив его на функции,
# каждая из которых решает
# свою конкретную задачу. Этот процесс называется рефакторингом (или переработкой).
# Рефакторинг делает ваш код более чистым, понятным и простым в расширении.


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
    username = input('Enter your name')
    filename = 'username_2.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Приветствует пользователя по имени"""
    username = get_stored_name()
    if username:
        print(f'Welcome back {username}')
    else:
        username = get_new_username()
        print(f'We will remember {username}')


greet_user()
