person_data_0 = {'first_name': 'Boris',
                 'last_name': 'Borodin',
                 'age': 22,
                 'city': 'Rostov-on-Don'
                 }
person_data_1 = {'first_name': 'Nikola',
                 'last_name': 'Tesla',
                 'age': 36,
                 'city': 'Colorado Springs',
                 }
person_data_2 = {'first_name': 'Anotoliy',
                 'last_name': 'Valasov',
                 'age': 29,
                 'city': 'Los Angeles',
                 }
users = [person_data_0,person_data_1,person_data_2]

for user in users:
    full_name = f"{user['first_name']} {user['last_name']}"
    print(f'{full_name} is {user.get("age")}, he lives in {user.get("city")}\n')