boddy = {'animal_type' : 'dog',
         'owner': 'Mark',
         }
jack = {'animal_type': 'parrot',
        'owner':'Simon'
        }
cookie = {'animal_type':'cat',
          'owner':'Lisa'
          }
pets = [boddy,jack,cookie]

for pet in pets:
    print(f'{pet["animal_type"]} owned to {pet["owner"]}')