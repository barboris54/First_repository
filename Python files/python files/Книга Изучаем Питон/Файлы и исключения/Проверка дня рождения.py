file_path = 'C:/Users/barbo/OneDrive/Рабочий стол/Файлы питон/text files/pi_million_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()


birth_day = input('inter your birthday without dots')
if birth_day.strip() in pi_string:
    print('Your bithdays is in pi number')
else:
    print('Your birthday not in pi number')

