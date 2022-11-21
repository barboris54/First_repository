# Одна из стандартных проблем при работе с файлами — отсутствие необходимых
# файлов. Тот файл, который вам нужен, может находиться в другом месте, в имени
# файла может быть допущена ошибка или файл может вообще не существовать.
# Все эти ситуации достаточно прямолинейно обрабатываются в блоках try-except

filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contens = f.read()
except FileNotFoundError:
    print(f'Sorry, file {filename} does not exist')
