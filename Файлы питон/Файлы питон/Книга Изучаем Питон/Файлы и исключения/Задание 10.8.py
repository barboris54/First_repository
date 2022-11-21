def name_pets(filename):
    """Выводит клички животных из файла"""
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        pass
    else:
        print(content)

names = ['Cats.txt','Dogs.txt']
for name in names:
    name_pets(name)