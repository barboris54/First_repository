requested_toppings = []
if requested_toppings: # Когда имя списка используется в условии if, Python возвращает True,
    # если список содержит хотя бы один элемент; если список пуст, возвращается значение False.
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}')
        print('\nFinished making your pizza')
else:
    print('\n Are your sure you want a plain pizza ?')

