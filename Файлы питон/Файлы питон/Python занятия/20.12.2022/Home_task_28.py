class Automobile:
    def __init__(self, model, year, manufactured, engine, color, price):
        self.model = model
        self.year = year
        self.manufactured = manufactured
        self.engine = engine
        self.color = color
        self.price = price

    def show_car_info(self):
        print('********* Данные автомобиля *********')
        print(f'Название модели: {self.model}')
        print(f'Год выпуска: {self.year}')
        print(f'Производитель: {self.manufactured}')
        print(f'Мощность двигателя: {self.engine}')
        print(f'Цвет: {self.color}')
        print(f'Цена: {self.price}')
        print('=' * 20)

    @staticmethod
    def verify_model(model):
        if not isinstance(model, str):
            raise TypeError('Модель должна быть строкой')

    @staticmethod
    def verify_year(year):
        if not isinstance(year, int):
            raise TypeError('Неверный формат')

    @staticmethod
    def verify_manufactured(manufactured):
        if not isinstance(manufactured, str):
            raise TypeError('Неверный формат')

    @staticmethod
    def verify_engine(engine):
        if not isinstance(engine, str):
            raise TypeError('Неверный формат')

    @staticmethod
    def verify_color(color):
        if not isinstance(color, str):
            raise TypeError('Неверный формат')

    @staticmethod
    def verify_price(price):
        if not isinstance(price, str):
            raise TypeError('Неверный формат')

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.verify_model(model)
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.verify_year(year)
        self.__year = year

    @property
    def manuf(self):
        return self.__manufactured

    @manuf.setter
    def manuf(self, manufactured):
        self.verify_manufactured(manufactured)
        self.__manufactured = manufactured

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine):
        self.verify_engine(engine)
        self.__engine = engine

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.verify_color(color)
        self.__color = color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.verify_price(price)
        self.__price = price


car1 = Automobile('X5', 2007, 'BMW', '220 л.с.', 'черный', '5000$')
car1.price = '10000$'
car1.show_car_info()
