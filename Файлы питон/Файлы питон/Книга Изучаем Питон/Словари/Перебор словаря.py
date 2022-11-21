user_0 = { 'user_name' : 'Nagibator228',
           'first_name' : 'Boris',
           'last_name' : 'Borodin',}
for keys, values in  user_0.items(): # .items возвращает список пар «ключ-значение»
    print(f'\nKey:{keys}')
    print(f'Values:{values}')

favorite_languages = {
    'jen' : 'java',
    'oliver' : 'c#',
    'simon' : 'Java',
    'bob' : 'python',
}
for name,language in favorite_languages.items():
    print(f'\nName:{name.title()}')
    print(f'Language:{language.title()}')