# Функция может вернуть любое значение, которое вам потребуется, в том числе
# и более сложную структуру данных (например, список или словарь). Так, следующая
# функция получает части имени и возвращает словарь, представляющий человека:

def buid_person(first_name, last_name,):
    """возвращает словарь с данными"""
    person = {f'fist :{first_name},last: {last_name}'}
    return person


musician = buid_person('jimmie', 'handrix',)
print(musician)
