def title(title):
    def wrapper(function):
        def wrap(*args, **kwargs):
            print(f' {title} '.center(50, '='))
            func = function(*args, **kwargs)
            print('=' * 50)
            return func

        return wrap

    return wrapper


class UserInterface:
    @title('Ввод пользывательских данных')
    def wait_user_answer(self):
        print('Действия с фильмами: ')
        print('1 - Добавление фильма'
              '\n2 - Каталог фильмов'
              '\n3 - просмотр определенного фильма'
              '\n4 - удаление фильма'
              '\nq - выход из программы')
        user_answer = input('Выберите вариант действия: ')
        return user_answer

    @title(' Добавление фильма ')
    def add_film(self):
        dict_film = {
            'Название: ': None,
            'Жанр: ': None,
            'Режиссер: ': None,
            'Год выпуска: ': None,
            'Длительность: ': None,
            'Студия: ': None,
            'Актеры: ': None
        }
        for key in dict_film:
            dict_film[key] = input(f'Введите {key} ')
        return dict_film

    @title('Список фильмов:')
    def show_all_films(self, films):
        for ind, film, in enumerate(films, start=1):
            print(f'{ind}. {film}')

    @title('Ввод названия фильма:')
    def get_certain_film(self):
        user_film = input('Введите название фильма:')
        return user_film

    def show_film_description(self, film):
        for key in film:
            print(f'{key} фильма - {film[key]}')

    @title('Сообщение об ошибке:')
    def show_incorrect_name_error(self, name):
        print(f'Фильма с названием {name} нет в каталоге')

    @title('Удаление фильма:')
    def remove_single_film(self, name):
        print(f'Фильм {name} удален из каталога')

    @title('Сообщение об ошибке:')
    def show_incorrect_answer_error(self, answer):
        print(f'Варианта {answer} не существует')
