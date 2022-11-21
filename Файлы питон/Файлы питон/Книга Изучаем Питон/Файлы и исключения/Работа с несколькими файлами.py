def count_words(filename):
    """Считает приблезительное количество слов в тексте"""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'Sorry, file {filename} does not exist !')
    else:
        """Подсчет приблизительного количества слов в тексте"""
        words = contents.split()
        print(len(words))


count_words('C:/Users/barbo/OneDrive/Рабочий стол/Файлы питон/text files/Cabala.txt')

filenames = ['guest.txt', 'guest_book.txt', 'programming.txt']
for filename in filenames:
    count_words(filename)
