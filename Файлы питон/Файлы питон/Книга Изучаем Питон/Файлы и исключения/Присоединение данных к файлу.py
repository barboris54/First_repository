# Если вы хотите добавить в файл новые данные вместо того, чтобы перезаписывать
# существующее содержимое, откройте файл в режиме присоединения. В этом случае Python не уничтожает содержимое файла перед возвращением объекта файла.
# Все строки, выводимые в файл, будут добавлены в конец файла. Если файл еще не
# существует, то Python автоматически создаст пустой файл.

filename = 'programming.txt'
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love make apps that can run in browser.\n")