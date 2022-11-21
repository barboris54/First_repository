sandwich_order = ['tuna sandwich', 'chicken sandwich', 'egg sandwich']
finished_sandwiches = []

while sandwich_order:
    made_sandwich = sandwich_order.pop()
    print(f'I made your {made_sandwich.capitalize()}!')

    finished_sandwiches.append(made_sandwich)

print('Follow sandwiches is already done:')
for finished_sandwiche in finished_sandwiches:
    print(f'\n\t{finished_sandwiche}')