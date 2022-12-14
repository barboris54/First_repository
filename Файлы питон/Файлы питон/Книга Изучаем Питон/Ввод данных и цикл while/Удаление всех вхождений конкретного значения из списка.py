# В главе 3 функция remove() использовалась для удаления конкретного значения
# из списка. Функция remove() работала, потому что интересующее нас значение
# встречалось в списке только один раз. Но что, если вы захотите удалить все вхождения значения из списка?
# Допустим, имеется список pets, в котором значение 'cat' встречается многократно.
# Чтобы удалить все экземпляры этого значения, можно выполнять цикл while до
# тех пор, пока в списке не останется ни одного экземпляра 'cat':
pet = ['cat', 'dog', 'parrot', 'cat', 'dolphin', 'cat']

while 'cat' in pet:
    pet.remove('cat')

print(pet)
