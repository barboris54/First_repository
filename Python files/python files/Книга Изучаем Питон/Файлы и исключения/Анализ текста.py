file_path = 'C:/Users/barbo/OneDrive/Рабочий стол/Файлы питон/text files/Cabala.txt'
filename = 'Cabala.txt'
try:
    with open(file_path,encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
     print(f'Sorry, file {filename} does not exist !')
else:
    """Подсчет приблизительного количества слов в тексте"""
    words = contents.split()
    print(len(words))

# Метод split() разделяет строку на части по всем позициям, в которых обнаружит
# пробел, и сохраняет все части строки в элементах списка. В результате создается
# список слов, входящих в строку (впрочем, вместе с некоторыми словами могут
# храниться знаки препинания.) Для подсчета слов в книге мы вызовем split()
# для всего текста, а затем подсчитаем элементы списка, чтобы получить примерное
# количество слов в тексте: