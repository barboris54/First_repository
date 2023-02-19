# Чтобы скопировать список, создайте сегмент, включающий весь исходный список
# без указания первого и второго индекса ([:]).
my_foods = ['apple', 'peach','plum','orange']
friends_food = my_foods[:]

print(f'My favorite foods are {my_foods}')
print((f'My friends favorite foods are {friends_food}\n'))

my_foods.append('ice cream')
friends_food.append('chocolate')

print(f'My favorite foods are {my_foods}')
print((f'My friends favorite foods are {friends_food}'))