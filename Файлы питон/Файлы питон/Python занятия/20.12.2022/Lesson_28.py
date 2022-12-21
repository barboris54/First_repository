class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x},{self.__y})'


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1) -> None:
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width

    def get_width(self):
        return self.__width


class Line(Prop):
    def __init__(self, *args):
        print("Переопределение иницализатора")
        super().__init__(*args)

    def draw_line(self):
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color},{self.get_width()}')


class Rect(Prop):
    def __init__(self, sp, ep, color='red', width=1, bg='yellow'):
        super().__init__(sp, ep, color, width)
        self._background = bg

    def draw_rect(self):
        print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.get_width()}, {self._background}')


line = Line(Point(1, 2), Point(10, 20))
line.draw_line()

rect = Rect(Point(30, 40), Point(70, 80))
rect.draw_rect()
