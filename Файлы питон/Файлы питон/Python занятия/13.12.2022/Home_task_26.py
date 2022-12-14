import math


class CountSquare:
    count_squares_term = 0

    @staticmethod
    def count_triangle_area_geron(*args):
        p = sum(args) // 2
        square = math.sqrt(p * (p - args[0]) + p * (p - args[1]) + p * (p - args[2]))
        CountSquare.count_squares_term += 1
        return square

    @staticmethod
    def count_triangle_area_h(*args):
        square = (args[0] * args[1]) // 2
        CountSquare.count_squares_term += 1
        return square

    @staticmethod
    def count_square_area(side):
        square = side**2
        CountSquare.count_squares_term += 1
        return square

    @staticmethod
    def count_rect_area(side1, side2):
        area = side1*side2
        CountSquare.count_squares_term += 1
        return area

    @staticmethod
    def show_count_terms():
        return CountSquare.count_squares_term


tr1 = CountSquare
print(tr1.count_triangle_area_geron(3, 4, 5))
print(tr1.count_triangle_area_h(6,7))
print(tr1.count_square_area(7))
print(tr1.count_rect_area(2,6))
print(CountSquare.show_count_terms())

