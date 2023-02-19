def print_models(unprinted_models,complite_models):
    while unprinted_models:
        current_print = unprinted_models.pop()
        print(f'Printing {current_print}')
        complite_models.append(current_print)
def show_completed_models(competed_models):
    """Выводит инофрмацию о всех напечатанных моделях"""
    print("Foollow models have been printed:")
    for complete_model in complete_models:
        print(complete_model)

unprinted_models = ['phone case','rorbot bendant', 'bibliarius']
complete_models = []
print_models(unprinted_models,complete_models)
show_completed_models(complete_models)