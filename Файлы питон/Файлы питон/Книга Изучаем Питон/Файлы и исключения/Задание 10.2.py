file_path = 'C:/Users/barbo/OneDrive/Рабочий стол/Файлы питон/text files/Python.txt'
with open(file_path) as file:
    lines = file.read()
    print(lines.replace('python','C'))