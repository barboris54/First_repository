class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты restaurant_name и cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}")
        print(f'It specializing on {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open !')

    def set_number_served(self, people):
        self.number_served = people

    def increase_number_served(self, plus_people):
        self.number_served += plus_people

    def read_number_served(self):
        print(f'This restaurant served {self.number_served} people today')


pan_asia = Restaurant('Pan asia', 'Asian cuisine')
pan_asia.describe_restaurant()
pan_asia.open_restaurant()
pan_asia.set_number_served(20)
pan_asia.increase_number_served(30)
pan_asia.read_number_served()
