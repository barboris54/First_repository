class Car():
    """Простая модель автомобиля"""

    def __init__(self, name, model, year):
        """Инициализирует атрибуты описания автомобиля"""
        self.name = name
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_describtive_name(self):
        long_name = f'{self.name} {self.model} {self.year}'
        return long_name

    def uptade_odometr(self, mileage):
        """Устанавливает заданное значение на одометре"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You cant roll back an odometer')

    def read_odometer(self):
        """ Показывает пробег в милях"""
        print(f'This car has {self.odometer_reading} miles on it')


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_describtive_name())

my_new_car.uptade_odometr(24)
my_new_car.read_odometer()
