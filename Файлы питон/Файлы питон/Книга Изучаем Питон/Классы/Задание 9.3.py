class User():
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} is {self.age} and he live in {self.city}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}\n')


user_1 = User('Alexander', 'Vlasenko', 21, 'Rostov-on-Don')
user_1.describe_user()
user_1.greet_user()
user_2 = User('Boris', 'Borodin', 22, 'Rostov-on-Don')
user_2.describe_user()
user_2.greet_user()
user_3 = User('Vano', 'Kevlishvily', 23, 'Tbilissi')
user_3.describe_user()
user_3.greet_user()
