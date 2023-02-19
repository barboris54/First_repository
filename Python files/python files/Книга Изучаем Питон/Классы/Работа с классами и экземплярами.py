# Классы могут использоваться для моделирования многих реальных ситуаций. После того как класс будет написан, разработчик проводит большую часть времени
# за работой с экземплярами, созданными на основе этого класса. Одной из первых
# задач станет изменение атрибутов, связанных с конкретным экземпляром. Атрибуты экземпляра можно изменять напрямую или же написать методы, изменяющие
# атрибуты по особым правилам.

class Car():
    """Простая модель автомобиля"""

    def __init__(self, name, model, year):
        """Инициализирует атрибуты описания автомобиля"""
        self.name = name
        self.model = model
        self.year = year
        self.odometer_read = 0

    def get_describtive_name(self):
        long_name = f'{self.name} {self.model} {self.year}'
        return long_name.title()

    def read_odometer(self):
        """ Показывает пробег в милях"""
        print(f'This car has {self.odometer_read} miles on it')


my_new_car = Car('Audi', 'A4', 2019)
print(my_new_car.get_describtive_name())
my_new_car.read_odometer()
