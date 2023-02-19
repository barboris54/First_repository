class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        """Инициализирует атрибуты restaurant_name и cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}")
        print(f'It specializing on {self.cuisine_type}')
    def open_restaurant(self):
        print(f'{self.restaurant_name} is open !')
restaurant = Restaurant('Pan Asia','Asian kitchen')
print(f'my favorite restaurant is {restaurant.restaurant_name}')
print(f'It specializing on {restaurant.cuisine_type}')
restaurant.describe_restaurant()
restaurant.open_restaurant()
