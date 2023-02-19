rivers = {'missisipi':'usa',
          'volga':'russia',
          'temza':'united kingdom'}
for river,countries in rivers.items():
    if countries == 'usa':
        print(f'{river.title()} run through {countries.upper()}')
    else:
        print(f'{river.title()} run through {countries.title()}')
    