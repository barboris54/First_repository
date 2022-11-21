person_data = {'first_name':'Boris',
               'last_name': 'Borodin',
               'age': 22,
               'city':'Rostov-on-Don'
               }
print(person_data)
first_name = person_data.get('first_name')
last_name = person_data['last_name']
age = person_data.get('age')
city = person_data['city']
print(f'{first_name} {last_name} is {age} years old and he live in {city}')

