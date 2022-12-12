import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def set_height(self, height):
        if isinstance(height, int):
            self.height = height
        else:
            print('Введеный параметр не является целым числом')

    def set_width(self, width):
        if isinstance(width, int):
            self.width = width
        else:
            print('Введеный параметр не является целым числом')

    def get_height(self):
        return print(f'Высота :{self.height}')

    def get_width(self):
        return print(f'Ширина: {self.width}')

    def get_rectagle_square(self):
        return print(f'Площадь: {self.height * self.width}')

    def get_rect_perimitr(self):
        return print(f'Периметр: {2 * (self.height + self.width)}')

    def get_rect_dioganal(self):
        return print(f'Диоганаль: {math.sqrt(self.width ** 2 + self.height ** 2)}')

    def print_rect(self):
        for i in range(self.height):
            for j in range(self.width):
                print('*',end='')
            print()


rect1 = Rectangle(3, 9)
rect1.get_height()
rect1.get_width()
rect1.get_rectagle_square()
rect1.get_rect_perimitr()
rect1.get_rect_dioganal()
rect1.print_rect()
