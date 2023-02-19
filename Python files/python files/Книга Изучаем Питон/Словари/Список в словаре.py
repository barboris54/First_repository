# Вместо того чтобы помещать словарь в список, иногда бывает удобно поместить
# список в словарь. Представьте, как бы вы описали в программе заказанную пиццу.
# Если ограничиться только списком, сохранить удастся разве что список топпингов
# к пицце. При использовании словаря список топпингов может быть всего лишь
# одним аспектом описания пиццы.

pizza = {'crust':'thick',
         'toppings': ['olive','extra cheese']}
print(f'You ordered {pizza.get("crust")}- pizza crust'
     'with following topings:')
for topping in pizza.get('toppings'):
    print('\t'+ topping) # !!!!

# Другой пример

favorite_languages = {
    'jen' : ['java','Python'],
    'oliver' : ['c#'],
    'bob' : ['python','c#']}
for name,languages in favorite_languages.items():
    if len(languages) == 1:
        print(f'{name.title()} like only')
        for language in languages:
            print(f'\t{language.title()}')
    else :
        print(f'{name.title()}s favorite languages:')
        for language in languages:
            print(f'\t{language.title()}')
