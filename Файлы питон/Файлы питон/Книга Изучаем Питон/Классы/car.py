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

    def increasement_odometer(self, miles):
        self.odometer_reading += miles

    def read_odometer(self):
        """ Показывает пробег в милях"""
        print(f'This car has {self.odometer_reading} miles on it')

    def fill_gas_tank(self):
        print('Your gas tank is full!')

class Battery():
    """Инициирует атрибуты аккумулятора"""

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_batery(self):
        """ Выодит информацию о мощности батареи"""
        print(f'This car have a {self.battery_size}-Kwh battery')

    def get_range(self):
        """Выводит приблезительный запас хода"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f'This car can move about {range} miles')


class ElectricCar(Car):
    """Представляет собой аспекты автомобиля, специфические для электромобилей"""

    def __init__(self, name, model, year):
        """ Инициализирует атрибуты класса родителя
        Затем инициализирует аттрибуты специфические для электромобиля"""
        super().__init__(name, model, year)
        self.battery = Battery(100)

    def fill_gas_tank(self):
        print('This car does not need a gas tank !')