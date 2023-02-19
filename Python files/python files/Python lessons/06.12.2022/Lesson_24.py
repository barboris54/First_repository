import os.path
import time

path = r'D:\pythonProject\Файлы питон\Файлы питон\Python занятия\04.12.2022\test\res1.txt'


# # print(os.path.exists(path))
# #
# print(os.path.getatime(path)) # возвращает время последнего доступа к файлу
# print(os.path.getctime(path)) # время создания файла
# print(os.path.getmtime(path)) # время последнего изменения
# print(os.path.getsize(path)) # размер файла в байтах

# size = print(os.path.getsize(path) / 1024)
# # print(size)
# t = print(os.path.getctime(path))
# pintr(time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(t)))

# print(os.path.isfile(path))
# print(os.path.isdir(path))

# class Point:
#     """Класс для представления координат на плоскости"""
#     x = 1
#     y = 1
#
#     def set_coord(self):
#         print('Метод set_coord')


# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))
#
# p1 = Point()
# print(p1.x)
# p1.x = 100
# print(p1.x)
# print(Point.x)

# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.z = 20
# print(p1.x, p1.y)
# print(p1.__dict__)


# class Point:
#     """Класс для представления координат на плоскости"""
#     x = 1
#     y = 1
#
#     def set_coord(self):
#         print(self.__dict__)
#
# p1 = Point()
# p1.x = 5
# p1.set_coord()

# class Point:
#     """Класс для представления координат на плоскости"""
#     x = 1
#     y = 1
#
#     def set_coord(self,x,y):
#         self.x = x
#         self.y = y
#
# p1 = Point()
# p1.set_coord(5,10)
# print(p1.__dict__)

class Human:
    name = 'name'
    birthday = '00.00.0000'
    phone = '0-000-000-00-00'
    country = 'country'
    city = 'city'
    adress = 'adress'

    def show_info(self):
        print(' Персональные данные '.center(40, '*'))
        print(
            f'Имя: {self.name}\nДата рождения: {self.birthday}\nНомер: {self.phone}\nСтрана: {self.country}\nГород: {self.city}\nАдрес: {self.adress}')
        print('=' * 40)

    def input_info(self, name, birthday, phone, country, city, adress):
        self.name = name
        self.birthday = birthday
        self.phone = phone
        self.country = country
        self.city = city
        self.adress = adress

    def set_name(self, name):
        if isinstance(name,str):
            self.name = name

    def get_name(self):
        return self.name



h1 = Human()
h1.show_info()
h1.input_info('Юля', '23.05.1986', '45-46-98', 'Россия', 'Москва', 'Чистропрудный бульвар 1А')
h1.show_info()
h1.set_name('helen')
h1.show_info()
print(h1.get_name())
print(h1.name)
