import json

main = {}
lst = []

while True:
    user_input = int(
        input('*************\nВыбор действия:\n1 - Добавление данных\n2 - Удаление данных\n3 - Поиск данных\n'
              '4 - Редактирование данных\n5 - Просмотр данных\n6 - Завершение работы\n Ввод - > '))

    if user_input == 1:
        capitals = {}
        input_country = input('Введите название страны с заглавной буквы: ')
        input_capital = input('Введите название столицы с заглавной буквы: ')
        capitals[input_country] = input_capital
        main[input_country] = capitals
        lst.append(input_country)
        print('Файл сохранен\n')

    if user_input == 2:
        input_del = input('Введите название страны которую хотите удалить с заглваной буквы: ')
        del main[input_del]
        lst.remove(input_del)
        print(f'Страна {input_del} удалена')

    if user_input == 3:
        find_elem = input('Введите страну которую хотите найти с заглавной буквы: ')
        print(f'Результат поиска:{main[find_elem]}\n')

    if user_input == 4:
        change_country = input('Введите название страны, которую хотите изменить с заглавной буквы: ')
        new_capital = input('Введите название столицы, которую хотите изменить с заглавной буквы: ')

        main[change_country] = {change_country: new_capital}
        print(f'Столица страны {change_country} была изменина на {new_capital}')

    if user_input == 5:
        try:
            with open('capitals.json', 'r') as f:
                a = (json.load(f))
                print('Текущие данные:')
                for i in a:
                    print(a[i])
        except FileNotFoundError:
            for i in lst:
                print(main[i])

    if user_input == 6:
        with open('capitals.json', 'w') as f:
            json.dump(main, f, indent=2)
        break
