sandwich_order = ['tuna sandwich', 'pastrami sandwich','chicken sandwich', 'egg sandwich','pastrami sandwich']
finished_sandwiches = []
print('Unfortunatelly we are run out of postrami')
while 'pastrami sandwich' in sandwich_order:
    sandwich_order.remove('pastrami sandwich')

while sandwich_order:
    made_sandwich = sandwich_order.pop()
    finished_sandwiches.append(made_sandwich)
for finished_sandwiche in finished_sandwiches:
    print('Following sandwiches is already done')
    print(f'\t{finished_sandwiche}')

    