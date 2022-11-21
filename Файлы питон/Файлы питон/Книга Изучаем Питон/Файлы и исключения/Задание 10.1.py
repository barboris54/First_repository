file_path = 'C:/Users/barbo/OneDrive/Рабочий стол/Файлы питон/text files/Python.txt'
with open (file_path) as file:
    lines = file.readlines()

    simple_line = ''
    for line in lines:
        simple_line += line.strip()

print(simple_line)

