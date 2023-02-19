from view_films import UserInterface
from model_films import FilmModel

class Controller:
    def __init__(self):
        self.film_model = FilmModel()
        self.film_view = UserInterface()

    def run(self):
        answer = None
        while answer !='q':
            answer = self.film_view.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == '1':
            film = self.film_view.add_film()
            self.film_model.add_film(film)
        elif answer == '2':
            films = self.film_model.get_all_films()
            self.film_view.show_all_films(films)
        elif answer == '3':
            film_name = self.film_view.get_certain_film()
            try:
                certain_film = self.film_model.get_single_film(film_name)
            except KeyError:
                self.film_view.show_incorrect_name_error(film_name)
            else:
                self.film_view.show_film_description(certain_film)
        elif answer == '4':
            film_name = self.film_view.get_certain_film()
            try:
                name = self.film_model.remove_film(film_name)
            except KeyError:
                self.film_view.show_incorrect_name_error(film_name)
            else:
                self.film_view.remove_single_film(film_name)

        elif answer == 'q':
            ...
        else:
             self.film_view.show_incorrect_answer_error(answer)





