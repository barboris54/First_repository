import math


class Table:
    def __init__(self, width=None, height=None, radius=None):
        self.width = width
        self.height = height
        self.radius = radius

    def find_area(self):
        raise NotImplementedError('Это функция должна быть во всех классах')


class RectTableArea(Table):
    def find_area(self):
        if self.width != self.height:
            return self.width * self.height
        if self.width == self.height:
            return self.width * self.width


class RoundTableArea(Table):
    def find_area(self):
        if self.radius:
            return self.radius ** 2 * math.pi
        else:
            raise ValueError('для подсчета площади круга нужно задать радиус !')


t1 = RectTableArea(20, 20, 300)
t2 = RoundTableArea(10, 20, 20)
print(t1.find_area())
print(t2.find_area())
