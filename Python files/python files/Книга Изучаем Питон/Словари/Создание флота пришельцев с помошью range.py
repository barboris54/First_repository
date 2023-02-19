#  Создание пустого списка для хранения пришельцев.
aliens = []

#  Создание 30 зеленых пришельцев.
for aliens_number in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'low'}
    aliens.append(new_alien)


# Вывод 5 пришельцев

for alien in aliens[:5]:
    print(alien)
print('...')

print(f'Total number of aliens:{len(aliens)}')

# Когда приходит время смены цветов, мы можем воспользоваться циклом for и командой if для изменения
# цвета

for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens[:5]:
    print(alien)
