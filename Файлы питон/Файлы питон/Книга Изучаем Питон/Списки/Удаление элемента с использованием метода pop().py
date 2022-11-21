# Метод pop() удаляет последний элемент из списка, но позволяет работать с ним после удаления

motocycles = ['honda','suzuki','yamaha']
popped_motocycles = motocycles.pop()
print(popped_motocycles)

# Вызов pop() может использоваться для удаления элемента в произвольной позиции
# списка; для этого следует указать индекс удаляемого элемента в круглых скобках.

motocycles_1 = ['honda','suzuki','yamaha']
popped_motocycles_1 = motocycles_1.pop(1)
print(f'The last motocycle I owned is {popped_motocycles_1}')