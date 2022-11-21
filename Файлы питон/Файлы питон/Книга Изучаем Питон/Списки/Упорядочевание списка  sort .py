# Метод sort() позволяет относительно легко отсортировать список, по алфавиту
cars = ['audi','bmw','toyota','honda']
cars.sort()
print(cars)
# Список также можно отсортировать в обратном алфавитном порядке; для этого
# методу sort() следует передать аргумент reverse=True.

cars.sort(reverse=True)
print(cars)