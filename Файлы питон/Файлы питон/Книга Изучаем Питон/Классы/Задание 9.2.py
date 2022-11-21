class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты restaurant_name и cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}")
        print(f'It specializing on {self.cuisine_type}\n')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open !')

restaurant_paris = Restaurant('Paris','French kitchen')
restaurant_paris.describe_restaurant()

restaurant_Tokyo = Restaurant('Tokyo','Japan kitchen')
restaurant_Tokyo.describe_restaurant()

restaurant_smetana = Restaurant('Smetana','Russian kitchen')
restaurant_smetana.describe_restaurant()