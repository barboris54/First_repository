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


class Privileges():
    def __init__(self):
        self.privileges = ['банить пользователей', 'блокировать чат', 'размещать рекламу']

    def show_privileges(self):
        print(f"You've got following privileges as Admin:")
        for privilege in self.privileges:
            print(f'\t{privilege}')


class Admin(User):
    def __init__(self, first_name, last_name, age, city, ):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()


admin = Admin('Boris', 'Borodin', 22, 'Toronto')
admin.privileges.show_privileges()
admin.describe_user()
