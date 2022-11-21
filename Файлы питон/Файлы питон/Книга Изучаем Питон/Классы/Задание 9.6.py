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

class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type, flavours,):
        super().__init__(restaurant_name,cuisine_type)
        self.flavours = flavours

    def show_flavours(self):
        print('We have following flavours:')
        for flavour in self.flavours:
            print(flavour)
backen_robbins = IceCreamStand('Backen Robbins','IceCream',['vanila','chocolate','rosberry'])
backen_robbins.describe_restaurant()
backen_robbins.show_flavours()