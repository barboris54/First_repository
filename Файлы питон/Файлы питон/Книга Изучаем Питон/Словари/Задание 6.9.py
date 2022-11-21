favorite_places = {'Tom' : ['Paris','Moscow','Han Hong'],
                   'Candies': ['Dupai','Miami','Salem'],
                   'Nick':['Greenwitch','Berlin','Milano']
                  }
for human,places in favorite_places.items():
        print(f'{human}s favorite places are:')
        for city in places:
            print(f'\t{city}')
