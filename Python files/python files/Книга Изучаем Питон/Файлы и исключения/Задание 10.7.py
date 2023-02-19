def name_pets(filename):
    """Выводит клички животных из файла"""
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        print(f'Sorry, file {filename} does not exist')
    else:
        print(content)

names = ['Cats.txt','Dogs.txt']
for name in names:
    name_pets(name)