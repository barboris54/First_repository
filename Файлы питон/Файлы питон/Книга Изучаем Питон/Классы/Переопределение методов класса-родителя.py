# Любой метод родительского класса, который в моделируемой ситуации делает не
# то, что нужно, можно переопределить. Для этого в классе-потомке определяется
# метод с тем же именем, что и у метода класса-родителя. Python игнорирует метод
# родителя и обращает внимание только на метод, определенный в потомке.

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



class ElectricCar(Car):
    """Представляет собой аспекты автомобиля, специфические для электромобилей"""

    def __init__(self, name, model, year):
        """ Инициализирует атрибуты класса родителя
        Затем инициализирует аттрибуты специфические для электромобиля"""
        super().__init__(name, model, year)
        self.battery_size = 75

    def describe_batery(self):
        """ Выодит информацию о мощности батареи"""
        print(f'This car have a {self.battery_size}-Kwh battery')

    def fill_gas_tank(self):
        print('This car does not need a gas tank !')


my_new_tesla = ElectricCar('tesla','model s',2019)
my_new_tesla.describe_batery()
my_new_tesla.fill_gas_tank()