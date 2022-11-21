alien_0 = {'colour': 'green', 'points': 5}
print(f' This alien colour is {alien_0["colour"]} ')

alien_0['colour'] = 'yellow'
print(f'This aliein colour is {alien_0["colour"]}')

alien_1 = {'x_position' : 0, 'y_posotion': 25, 'speed': 'medium'}
print(f'Orginal x_posotion: {alien_1["x_position"]}')

# пришелец перемещаеться вправо.
# dsxbckztv позицию пришельца с учетом скорости смещения

if alien_1['speed'] == 'low':
    x_increasement = 1
elif alien_1['speed'] == 'medium':
    x_increasement = 2
else:
    x_increasement == 3
alien_1['x_position'] = alien_1['x_position'] + x_increasement
print(f'New x_position is {alien_1["x_position"]}')