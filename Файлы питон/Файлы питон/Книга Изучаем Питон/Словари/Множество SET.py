# Чтобы получить список выбранных языков без повторений, можно воспользоваться множеством
# (set). Множество в целом похоже на список, но все его элементы должны быть
# уникальными:
favorite_languages = {
    'jen' : 'java',
    'oliver' : 'c#',
    'simon' : 'java',
    'bob' : 'python',}

print('\tThis languages have been mentioned:')

for language in set ((favorite_languages.values())):
    print(f'{language}')

