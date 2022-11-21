requested_toppings = ['mushrooms', 'green pepper','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green pepper':
        print('Sorry we are out of green pepper')
    else:
        print(f'Adding {requested_topping}')
print('\nFinished making your pizza')