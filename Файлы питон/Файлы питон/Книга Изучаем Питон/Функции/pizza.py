def make_pizza(size,*toppings):
    print(f'\tMaking {size} - inch pizza with following topping:')
    for topping in toppings:
        print(f'-{topping}')