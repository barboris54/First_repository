def print_models(unprinted_models,complite_models):
    while unprinted_models:
        current_print = unprinted_models.pop()
        print(f'Printing {current_print}')
        complite_models.append(current_print)