my_pizzas = ['margarita', '4cheese', 'BBQ']
friends_pizzas = my_pizzas[:]
print(friends_pizzas)
my_pizzas.append('margarita')
friends_pizzas.append('havai')
for menu in my_pizzas:
    print(menu)
print('My favorite pizzas')
for menu_1 in friends_pizzas:
    print(menu_1)
print('Friends favorite pizzas')