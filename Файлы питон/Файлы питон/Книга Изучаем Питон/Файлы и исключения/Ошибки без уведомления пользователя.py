# В предыдущем примере мы сообщили пользователю о том, что один из файлов оказался недоступен. Тем не менее вы не обязаны сообщать о каждом обнаруженном
# исключении. Иногда при возникновении исключения программа должна просто
# проигнорировать сбой и продолжать работу, словно ничего не произошло. Для
# этого блок try пишется так же, как обычно, но в блоке except вы явно приказываете Python не предпринимать никаких особых действий в случае ошибки. В языке
# Python существует команда pass, с которой блок ничего не делает:

def count_words(filename):
    """Считает приблезительное количество слов в тексте"""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        """Подсчет приблизительного количества слов в тексте"""
        words = contents.split()
        print(len(words))


count_words('C:/Users/barbo/OneDrive/Рабочий стол/Файлы питон/text files/Cabala.txt')

filenames = ['guest.txt', 'guest_book.txt', 'programming.txt']
for filename in filenames:
    count_words(filename)