# Чтобы сохранить исходный порядок элементов списка, но временно представить их
# в отсортированном порядке, можно воспользоваться функцией sorted(). Функция
# sorted() позволяет представить список в определенном порядке, но не изменяет
# фактический порядок элементов в списке

cars = ['audi','bmw','toyota','honda']
print('Here is orgonal list of cars:')
print(cars)

print('\nHere is the sorted list')
print(sorted(cars))

print('\nHere is orgonal list of cars again:')
print(cars)