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
    @title('Ввод пользовательских данных')
    def wait_user_answer(self):
        print('Действия со статьями:')
        print('1 - Создание статьи'
              '\n2 - просмотр статей'
              '\n3 - просмотр определенной статьи'
              '\n4 - удаление статьи'
              '\nq - выход из программы')
        user_answer = input('Выберите вариант действия: ')
        return user_answer
    @title('Создание статьи')
    def add_user_article(self):
        dict_article = {
            'Название': None,
            'Автор': None,
            'Количество страниц': None,
            'Описание': None
        }
        for key in dict_article:
            dict_article[key] = input(f'Введите {key} статьи: ')
        return dict_article
    @title('Список статей:')
    def show_all_articles(self, article):
        for ind, article in enumerate(article, start=1):
            print(f'{ind}. {article}')
    @title('Введите название статьи')
    def get_user_article(self):
        user_article = input('Введите название статьи: ')
        return user_article
    @title('Просмотр статьи')
    def show_single_article(self, article):
        for key in article:
            print(f'{key} статьи - {article[key]}')

    def show_incorrent_title_error(self, title):
        print(f'Статьи с названием {title} не существует \n')

    @title('Удаление статьи:')
    def removr_single_article(self, article):
        print(f'Статья с название {article} была удалена')

    @title('Сообщение об ошибке:')
    def show_incorrect_asnwer_error(self, answer):
        print(f'Вариант {answer} не существует')
