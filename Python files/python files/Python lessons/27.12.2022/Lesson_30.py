from abc import ABC, abstractmethod


# class Chess(ABC):
#     def draw(self):
#         print('нарисовал шахматную фигуру')
#
#     @abstractmethod
#     def move(self):
#         pass
#
#
# class Queen(Chess):
#     def move(self):
#         print('Переместил фигуру')
#
#
# q = Queen()
# q.move()
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=' ')
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
#
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# for elem in e:
#     elem.print_value()
#     print(f'{elem.convert_to_rub():.2f} RUB')

# Интерфейсы__________________________________________________________________________

#
# class Father:
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
# class Child(Father):
#     def display1(self):
#         print('Дочерный класс')
#
#
# class GrandChild(Child):
#     def display2(self):
#         print('Внучатый класс')
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()

# Вложенные классы ______________________________________________________________
#
# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_class_method():
#         print('Я метод внешнего класса')
#
#     def outer_obj_method(self):
#         print('Связующий метод')
#
#     class MiInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print('Я метод вложенного класса', MyOuter.age, self.obj.name)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('внешний')
# inner = out.MiInner('внутренний', out)
# # print(out.name)
# # print(inner.inner_name)
# inner.inner_method()

class Color:
    def __init__(self):
        self.name = 'green'
        self.lg = self.LightGreen()

    def show(self):
        print('Name:', self.name, self.lg.code)

    class LightGreen:
        def __init__(self):
            self.name = 'Light green'
            self.code = '024avc'

        def display(self):
            print('Name:', self.name)
            print('Code:', self.code)

outer = Color()
outer.show()

g = outer.lg
g.name = 'Red'
g.display()