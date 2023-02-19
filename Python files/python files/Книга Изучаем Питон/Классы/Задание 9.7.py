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


class Admin(User):
    def __init__(self, first_name, last_name, age, city, privileges):
        super().__init__(first_name, last_name, age, city)
        self.privileges = privileges

    def show_privileges(self):
        print(f"You've got following privileges as Admin:")
        for privilege in self.privileges:
            print(f'\t{privilege}')

admin = Admin('Boris','Borodin',22,'Rostov', ['банить пользователей', 'блокировать чат', 'размещать рекламу'])

admin.age = 25
admin.describe_user()
admin.greet_user()
admin.show_privileges()