glossary = {'Список': 'это массив хранящий в себе какие-то данные',
            'строка': 'это тип данных который может содержать любую информацию заключенную в кавычки',
            'Кортеж ': 'это массив, хранящий в себе какие-то данные, но в отличии от списка кортежи неизменяемые',
            'переменная': 'это ячейка памятика храняшая в себе ссылку на какую-то другую информацию',
            'цикл': 'это определенная функция в языке которая позволяет переберать итеррируемые объекты'
}
spisok = glossary.get('Список')
string = glossary.get('строка')

print(f'Строка - \n\t{string}\n Список -\n\t{spisok}')