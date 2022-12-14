# Работа над новым классом не обязана начинаться с нуля. Если класс, который
# вы пишете, представляет собой специализированную версию ранее написанного
# класса, вы можете воспользоваться наследованием. Один класс, наследующий от
# другого, автоматически получает все атрибуты и методы первого класса. Исходный
# класс называется родителем, а новый класс — потомком. Класс-потомок наследует
# атрибуты и методы родителя, но при этом также может определять собственные
# атрибуты и методы

# При написании нового класса на базе существующего класса часто приходится вызывать метод __init__() класса-родителя. При этом происходит инициализация
# любых атрибутов, определенных в методе __init__() родителя, и эти атрибуты
# становятся доступными для класса-потомка.

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

class ElectricCar(Car):
    """Представляет собой аспекты автомобиля, специфические для электромобилей"""
    def __init__(self,name,model,year):
        """ Инициализирует атрибуты класса родителя"""
        super().__init__(name,model,year)

# Функция super() в строке  — специальная функция, которая позволяет вызвать метод родительского класса. Эта строка приказывает Python вызвать метод
# __init__() класса Car, в результате чего экземпляр ElectricCar получает доступ ко всем атрибутам класса-родителя.

my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_describtive_name())




