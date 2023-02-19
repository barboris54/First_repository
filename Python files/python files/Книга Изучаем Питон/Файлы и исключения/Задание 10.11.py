import json


def show_number():
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)

    except FileNotFoundError:
        return None
    else:
        return number


def get_fovorite_number():
    filename = 'favorite_number.json'
    favorite_number = int(input('Enter your favorite number'))
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    return favorite_number


def read_number():
    """Показывает любимую цифру """
    favorite_number = show_number()
    if favorite_number:
        print(f'I know your favorite number is {favorite_number}')
    else:
        favorite_number = get_fovorite_number()
        print(f'I will remember your number is {favorite_number}')

read_number()