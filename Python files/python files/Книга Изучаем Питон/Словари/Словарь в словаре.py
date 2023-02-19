users = {
    'Agrol': {
        'first_name':'Wiliam',
        'last_name':'Brown',
        'city':'London,'
    },
    'Domer': {
        'first_name': 'Simon',
        'last_name': 'Tailor',
        'city': 'Los Angeles'
    },
}
for user_name,user_info in users.items():
    full_name = f'{user_info.get("first_name")} {user_info["last_name"]}'
    print(f'{user_name} real name is {full_name}')
    print(f'{full_name} live in {user_info["city"]}')