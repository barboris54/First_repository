class Book:
    title = 'title'
    year = '0000'
    publisher = 'publisher'
    janra = 'janra'
    author = 'author'
    price = '10$'

    def show_book_info(self):
        print(
            f'Название книги: {self.title}\nГод выпуска: {self.year}\nИздатель: {self.publisher}\nЖанр: {self.janra}\nАвтор: {self.author}\nЦена: {self.price}')

    def input_book_info(self, title, year, publ, janra, author, cost):
        self.title = title
        self.year = year
        self.publisher = publ
        self.janra = janra
        self.author = author
        self.price = cost

    def set_book_title(self, title):
        self.title = title

    def get_book_title(self):
        return self.title

    def set_book_year(self, year):
        self.year = year

    def get_book_year(self):
        return self.year

    def set_book_publisher(self, publ):
        self.publisher = publ

    def get_book_publiser(self):
        return self.publisher

    def set_book_janra(self, janra):
        self.janra = janra

    def get_book_janra(self):
        return self.janra

    def set_book_author(self, author):
        self.author = author

    def get_book_author(self):
        return self.author

    def set_book_price(self, price):
        self.price = price

    def get_book_price(self):
        return self.price

book1 = Book()
book1.input_book_info('Danwich Horor', '1935', 'Weird Tales', 'Horror', 'Govard P. Lovecraft', '2$')
book1.show_book_info()
book1.set_book_price('3$')
print(book1.get_book_price())
book1.show_book_info()

