import os.path
with open('DZ.txt', 'r+', encoding='UTF-8') as f:
    a = (list(f))
    print(a)
    pos1 = int(input('введите номер строки которую хотите заменить от 0 до 3 '))
    pos2 = int(input('введите номер строки на которую хотите заменить от 0 до 3 '))
    a[pos1], a[pos2] = a[pos2], a[pos1]
    print(a)

with open('DZ.txt', 'w', encoding='UTF-8') as f:
    for i in a:
        f.writelines(i)


