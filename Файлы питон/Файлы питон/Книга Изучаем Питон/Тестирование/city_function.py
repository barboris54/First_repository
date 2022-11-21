def country_city(country, city, population=''):
    '''возвращает отформатированное сообщения типо Город.Страна'''
    if population:
        formated_message = f'{country}, {city} - population {population}'
    else:
        formated_message = f'{country}, {city}'
    return  formated_message.title()
