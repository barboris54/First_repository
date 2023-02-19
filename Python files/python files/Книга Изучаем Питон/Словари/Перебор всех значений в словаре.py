# Если вас прежде всего интересуют значения, содержащиеся в словаре, используйте
# метод values() для получения списка значений без ключей

favorite_languages = {
    'jen' : 'java',
    'oliver' : 'c#',
    'simon' : 'Java',
    'bob' : 'python',}
print('\tThis languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())