aviable_toppings = ['mushrooms', 'extra cheese', 'green pepper',
                    'peperoni', 'olives', 'pineapples']
requested_toppings = ['olives', 'french fries', 'green pepper']
for requested_topping in requested_toppings:
    if requested_topping in aviable_toppings:
        print(f'Adding {requested_topping}')
    else:
        print(f"Sorry {requested_topping} topping in not aviable")
print('\nFinished making your pizza')
