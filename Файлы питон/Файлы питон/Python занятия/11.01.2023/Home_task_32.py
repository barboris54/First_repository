import random

sex1 = ['F', 'M']


class Cat:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        if self.sex == 'M':
            print(f'{self.name} is a good boy!')
        else:
            print(f'{self.name} is a good girl!')

    def __add__(self, other):
        if self.sex + other.sex:
            return [Kitten(sex=random.choice(sex1)).__str__() for _ in range(random.randint(1, 5))]


class Kitten:
    def __init__(self, name='No name', age=0, sex='M'):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return f'Cat("name" = {self.name}, "age" = {self.age}, "sex" = {self.sex})'


c1 = Cat('Garfield', 9, 'M')
c2 = Cat('Lizz', 7, 'M')
c3 = c1 + c2
print(c3)
