# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# # print(r1.get_per_rect(), r2.get_per_rect())
#
# s1 = Square(10)
# s2 = Square(20)
#
# # print(s1.get_per_sq(), s2.get_per_sq())
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s2, s1, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())

# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
# t1 = Number(10)
# t2 = Text('Python')
#
# print(t1.total(10))
# print(t2.total(35))

# class Cat:
#     def __init__(self, type, name, age):
#         self.type = type
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f'Я {self.type}. Меня зовут {self.name}. Мне {self.age} лет.')
#
#     def make_sound(self):
#         print(f'{self.name} мяукает')
#
#
# class Dog:
#     def __init__(self, type, name, age):
#         self.type = type
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f'Я {self.type}. Меня зовут {self.name}. Мне {self.age} лет.')
#
#     def make_sound(self):
#         print(f'{self.name} гавкает')
#
#
# cat = Cat('Кот', 'Рыжик', 2.5)
# dog = Dog('Собака', 'Шарик', 3.5)
#
# animals = [cat,dog]
# for i in animals:
#     i.show_info()
#     i.make_sound()

# class Human:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#     def info(self):
#         print('\n', self.name, self.surname, self.age, end=' ')
#
#
# class Student(Human):
#     def __init__(self, name, surname, age, occupation, group, mark):
#         super().__init__(name, surname, age)
#         self.occupation = occupation
#         self.group = group
#         self.mark = mark
#
#     def info(self):
#         super().info()
#         print(self.occupation, self.group, self.mark, end=' ')
#
#
# class Teacher(Human):
#     def __init__(self, name, surname, age, occupation, raiting):
#         super().__init__(name, surname, age)
#         self.occupation = occupation
#         self.raiting = raiting
#
#     def info(self):
#         super().info()
#         print(self.occupation, self.raiting, end=' ')
#
#
# class Graduate(Student):
#     def __init__(self, name, surname, age, occupation, group, mark, final):
#         super().__init__(name, surname, age, occupation, group, mark)
#         self.final = final
#
#     def info(self):
#         super().info()
#         print(self.final, end=' ')
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group:
#     i.info()
#
# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def __repr__(self):
#         return f'{self.__class__}: {self.name}'
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# cat = Cat('Пушок')
# print(cat)

# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
# p = Point(5, 7)
# print(len(p))
#
# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y, ):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# pt = Point(1, 2)
# print(pt.length)
# # pt.z = 3
# # print(pt.__dict__)

# Функторы________________________________________________________________

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()

class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError('Аргумент должен быть строкой')

        return args[0].strip(self.__chars)


s1 = StripChars('?:!.;')
print(s1('Hello World!'))