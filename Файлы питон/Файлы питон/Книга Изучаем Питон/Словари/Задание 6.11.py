cities = {
    'rostov':
        {'country': 'russia',
         'population': '1 million',
         'fact': 'Don casaks lived in Rostov'},
    'london':
        {'country':'england',
         'population': '4 millions',
         'fact': 'London Tower is here'},
    'tokyo':
        {'country': 'japan',
         'population': '14 millions',
         'fact': ' this is Anime capital'}

}
for city, city_info in cities.items():
    print(
        f'{city.title()} is situated in {city_info.get("country").title()},its population is {city_info.get("population")}'
        f'and it is interesting to know that {city_info.get("fact")}')
