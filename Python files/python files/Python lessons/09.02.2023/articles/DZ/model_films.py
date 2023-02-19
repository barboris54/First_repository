class Film:
    def __init__(self, name, janra, director, year, duration, studio, actors):
        self.name = name
        self.janra = janra
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f'{self.name}, directed by {self.director}, ({self.year})'


class FilmModel:
    def __init__(self):
        self.films = {}

    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.films[film.name] = film

    def get_all_films(self):
        return self.films.values()

    def get_single_film(self, name):
        film = self.films[name]
        dict_films = {
            'Название: ': film.name,
            'Жанр: ': film.janra,
            'Режиссер: ': film.director,
            'Год выпуска: ': film.year,
            'Длительность: ': film.duration,
            'Студия: ': film.studio,
            'Актеры: ': film.actors
        }
        return dict_films

    def remove_film(self, name):
        return self.films.pop(name)