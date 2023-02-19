class Dog():
    """Простоая модель собаки"""

    def __init__(self,name,age):
        """Инициализурует атрибуты name и age"""
        self.name = name
        self.age = age
    def sit(self):
        """Собака садиться по команде"""
        print(f'{self.name} is now sitting')
    def roll_over(self):
        """Собака перекатываеться по команде"""
        print(f'{self.name} rolled over !')


# После создания экземпляра на основе класса Dog можно применять точечную
# запись для вызова любых методов, определенных в Dog:

my_dog = Dog('willie',6)

my_dog.sit()
my_dog.roll_over()

