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


my_dog = Dog('willie',6)
print(f'My dogs name is {my_dog.name}')
print(f'{my_dog.name} is {my_dog.age} years old')
my_dog.sit()

your_dog = Dog('lucy',3)
print(f'\nMy dogs name is {your_dog.name}')
print(f'{your_dog.name} is {your_dog.age} years old')
your_dog.sit()