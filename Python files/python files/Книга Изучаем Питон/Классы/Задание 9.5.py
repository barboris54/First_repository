class User():
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.loggin_attemps = 0

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} is {self.age} and he live in {self.city}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}\n')

    def increasement_login_atteps(self):
        self.loggin_attemps += 1

    def reset_loggin_attemps(self):
        self.loggin_attemps = 0


    def read_user_attemps(self):
        print(f'This user try to log in for {self.loggin_attemps} times')


human = User('boris','borodin',22,'rostov')
human.increasement_login_atteps()
human.increasement_login_atteps()
human.read_user_attemps()
human.reset_loggin_attemps()
human.read_user_attemps()