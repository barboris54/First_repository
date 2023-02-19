# Иногда позиция удаляемого элемента неизвестна. Если вы знаете только значение
# элемента, используйте метод remove()

motocycles = ['honda', 'suzuki', 'yamaha', 'ducati']
motocycles.remove('ducati')
print(motocycles)

too_expensive = 'honda'
motocycles.remove(too_expensive)
print(f'\nA {too_expensive.title()} \ntoo expensive for me')
