def country_city(country, city):
    country_and_city = f'{country}, {city}'
    return country_and_city.title()


while True:
    print('If you want to stop enter q')
    countr = input('Enter city').strip()
    if countr == 'q':
        break
    cit = input('Input country').strip()
    if  cit == 'q':
        break
    result = country_city(cit, countr)
    print(result)
