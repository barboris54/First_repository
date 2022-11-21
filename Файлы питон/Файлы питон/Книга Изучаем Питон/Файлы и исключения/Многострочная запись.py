# Функция write() не добавляет символы новой строки в записываемый текст. А это
# означает, что если вы записываете сразу несколько строк без включения символов
# новой строки, полученный файл может выглядеть не так, как вы рассчитывали

filename = 'programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# Если включить символы новой строки в команды write(), текст будет состоять из
# двух строк