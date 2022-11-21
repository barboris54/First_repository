
from car import ElectricCar


my_tesla = ElectricCar('Tesla','Model S',2019)
print(my_tesla.get_describtive_name())
my_tesla.battery.describe_batery()
my_tesla.battery.get_range()