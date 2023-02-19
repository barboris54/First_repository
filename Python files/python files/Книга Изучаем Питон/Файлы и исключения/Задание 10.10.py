file_path = 'C:/Users/barbo/OneDrive/Рабочий стол/Файлы питон/text files/Cabala.txt'
with open(file_path) as f:
    content = f.read()
    print(content.lower().count('the '))