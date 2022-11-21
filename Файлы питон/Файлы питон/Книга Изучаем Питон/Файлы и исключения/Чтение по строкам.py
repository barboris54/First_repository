file_path = 'C:/Users/barbo/OneDrive/Рабочий стол/Файлы питон/text files/pi_digits.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())
