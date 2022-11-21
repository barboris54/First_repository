topping =('What topping do you want ?')
topping += 'if you wont toppings enter quit'

activ = True
while activ:
    add_topping = input(topping).strip()
    if add_topping == 'quit':
        activ = False
    else:
        print(f'{add_topping.title()} now is adding into your order')