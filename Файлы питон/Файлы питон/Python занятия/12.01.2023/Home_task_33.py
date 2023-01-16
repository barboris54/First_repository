import math


class Shape:
    def __init__(self, color):
        self.color = color

    def perimetr(self):
        pass

    def area(self):
        pass

    def draw(self):
        raise NotImplementedError

    def show_info(self):
        raise NotImplementedError


class Square(Shape):
    def __init__(self, color, side1):
        super().__init__(color)
        self.side = side1

    def perimetr(self):
        return self.side * 4

    def area(self):
        return self.side * self.side

    def draw(self):
        for i in range(self.side):
            for j in range(self.side):
                print('*', end='')
            print()

    def show_info(self):
        print("====Квадрат=====")
        print(f'Периметр: {self.perimetr()}')
        print(f'Площадь: {self.area()}')
        print(f'Цвет: {self.color}')
        self.draw()


class Rect(Shape):
    def __init__(self, color, side1, side2):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2

    def perimetr(self):
        return (self.side1 + self.side2) * 2

    def area(self):
        return self.side1 * self.side2

    def draw(self):
        for i in range(self.side1):
            for j in range(self.side2):
                print('*', end='')
            print()

    def show_info(self):
        print("====Прямоугольник=====")
        print(f'Периметр: {self.perimetr()}')
        print(f'Площадь: {self.area()}')
        print(f'Цвет: {self.color}')
        self.draw()


class Triangle(Shape):
    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimetr(self):
        return (self.side1 + self.side2 + self.side3)

    def area(self):
        p = self.perimetr() / 2
        return round(math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3)), 2)

    def draw(self):
        for i in range(self.side2):
            print(' ' * (self.side2 - 1 - i) + '*' * (1 + i * 2))

    def show_info(self):
        print("====Треугольник=====")
        print(f'Периметр: {self.perimetr()}')
        print(f'Площадь: {self.area()}')
        print(f'Цвет: {self.color}')
        self.draw()


s1 = Square('red', 3)
s1.show_info()

r1 = Rect('blue', 4, 6)
r1.show_info()

t1 = Triangle('yellow', 11, 6, 6)
t1.show_info()
