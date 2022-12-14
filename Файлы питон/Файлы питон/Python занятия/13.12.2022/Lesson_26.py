# class Point:
#     __slots__ = ['__y', '__x']
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def set_coord_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print('координаты должны быть числами')
#
#     def set_coord_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print('координаты должны быть числами')
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def get_coord_x(self):
#         return self.__x
#
#     def get_coord_y(self):
#         return self.__y
#
#
# p1 = Point(11, 10)
# print(p1.get_coord_x())
# p1.set_coord_y(22)
# print(p1.get_coord_y())

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         print('Вызов__set_x')
#         self.__x = x
#
#     def __get_x(self):
#         print('вызов __get_x')
#         return self.__x
#
#     def __del_x(self):
#         print('Удаление свойста')
#         del self.x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         print('вызов __get_x')
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         print('Вызов__set_x')
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         print('Удаление свойста')
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются только числами')
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg)
# print(weight.to_pounds())
#
# class Person:
#     def __init__(self, name, skill):
#         self.__name = name
#         self.__skill = skill
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,name):
#         if isinstance(name,str):
#             self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def skill(self):
#         return self.__skill
#
#     @skill.setter
#     def skill(self, skill):
#         if isinstance(skill, str):
#             self.__skill = skill
#
#     @skill.deleter
#     def skill(self):
#         del self.__skill
#
# p1 = Person('Victor','12')
# print(p1.name, p1.skill)
# p1.name = 'Boris'
# p1.skill = '228'

# class Point:
#     __count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_coutn():
#         return Point.__count
#
#
# p1 = Point(5, 10)
# p2 = Point(4, 8)
# p3 = Point(3, 6)
# print(Point.get_coutn())

# import math
#
#
# class Count:
#     @staticmethod
#     def min_num(*args):
#         return min(*args)
#
#     @staticmethod
#     def max_num(*args):
#         return max(*args)
#
#     @staticmethod
#     def midle(*args):
#         return sum(args) // len(args)
#
#     @staticmethod
#     def facorial(x):
#         return math.factorial(x)
#
#
# print(Count.min_num(2, 5, 7, 1))
# print(Count.max_num(2, 5, 7, 1))
# print(Count.midle(2, 5, 7, 1))
# print(Count.facorial(5))

class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.moth = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('.'))
        date1 = cls(day, month, year)
        return date1

    def string_to_db(self):
        return f'{self.year}-{self.moth}-{self.day}'



string_date = Data.from_string('23.10.2022')

date = Data.from_string('23.10.2022')
print(string_date.string_to_db())
