# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print(f'Имя сотрудника: {self.name} {self.surname}')
#
#     def add_skill(self, k):
#         self.skill += k
#         print(f'квалификация сотрудника = {self.skill}\n')
#
#
# p1 = Person('Viktor', 'Reznik')
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person('Anna', 'Dolgih')
# p2.print_info()
# p2.add_skill(2)

# class Point:
#     # def __new__(cls, *args, **kwargs):
#     #     print('Конструктор')
#     #     return super().__new__(cls)
#
#     def __init__(self, x, y):
#         print('Инициализатор')
#         self.x = x
#         self.y = y
#
#
#     def __del__(self):
#         print('Удаление экземпляра', self.__class__.__name__)
#
#     def print_coords(self):
#         print(f'x: {self.x}, y: {self.y}')
#
# p1 = Point(5,10)
# p1.print_coords()
#
# p2 = Point(2,7)
# del p2
# p2.print_coords()


# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# print(p1.count)
# p2 = Point(7, 2)
# print(p2.count)

# class Robot:
#     robot_count = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f'Инициализация робота: {self.name}')
#         Robot.robot_count += 1
#
#     def __del__(self):
#         print(f'Робот {self.name} выключается !')
#         Robot.robot_count -= 1
#         if Robot.robot_count == 0:
#             print(f'Робот {self.name} был последним. ')
#         else:
#             print('Работающих роботов осталось:',Robot.robot_count )
#
#     def say_hi(self):
#         print(f'Hello I am {self.name}')
#
#
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print('Количество роботов:' ,droid1.robot_count)
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print('Количество роботов:' ,droid2.robot_count)
#
# print('\nЗдесь роботы закончили свою работу\n')
# del droid1
# del droid2
# print(f'Численность роботов: {Robot.robot_count}')

# Инкапсуляция __________________________________________________________________________________________________________________

class Point:
    def __init__(self, x, y):
        self.__x = self.__y = 0
        if Point.__check_value(x) and Point.__check_value(y):
            self.__x = x
            self.__y = y

    def set_coord_x(self, x):
        if Point.__check_value(x):
            self.__x = x
        else:
            print('координаты должны быть числами')

    def set_coord_y(self, y):
        if Point.__check_value(y):
            self.__y = y
        else:
            print('координаты должны быть числами')

    def __check_value(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    def get_coord_x(self):
        return self.__x

    def get_coord_y(self):
        return self.__y


p1 = Point(11, 10)
print(p1.get_coord_x())
p1.set_coord_y(22)
print(p1.get_coord_y())

# p1.x = 100
# p1.y = 'abc'
# print(p1.x, p1.y)
