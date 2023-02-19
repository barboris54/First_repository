 # Один из способов получения элементов в определенном порядке основан на сортировке ключей, возвращаемых циклом for. Для получения упорядоченной копии
 # ключей можно воспользоваться функцией sorted():

favorite_languages = {
    'jen' : 'java',
    'oliver' : 'c#',
    'simon' : 'Java',
    'bob' : 'python',}

for name in sorted(favorite_languages.keys()):
    print(f'{name.title()} thank you for taking the poll')