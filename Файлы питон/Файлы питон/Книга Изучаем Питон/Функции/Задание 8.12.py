def make_sandwich(bread,ham,*another_ingridiens):
    print(f'Your sandwich concist of {bread},{ham} and folowing ingridients:')
    for ingridient in another_ingridiens:
        print(f'\t {ingridient}')
make_sandwich('bread','ham','ketchup','mayoneese','salat')