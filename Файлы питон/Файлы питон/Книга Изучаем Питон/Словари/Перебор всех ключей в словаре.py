favorite_languages = {
    'jen' : 'java',
    'oliver' : 'c#',
    'simon' : 'Java',
    'bob' : 'python',}
for key in favorite_languages.keys(): # метод .keys() вызывает только ключи из словаря
    print(f'{key} take part in this')

# На самом деле перебор ключей используется по умолчанию при переборе словаря,
# так что этот код будет работать точно так же, как если бы вы написали
# for name in favorite_languages

friends = ['oliver', 'bob']
for name in favorite_languages.keys():
    if name in friends:
        language = favorite_languages[name]
        print(f"{name.title()}'s favorite language is {language.title()}! ")