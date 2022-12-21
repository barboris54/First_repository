# Задача 1
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB.'
#     suffix_usd = 'USD.'
#     suffix_eur = 'EUR.'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f'Счет #{self.num} принадлежащий {surname} был открыт.')
#         print("*" * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def edit_owner(self,surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def print_balance(self):
#         print(f'Текущий баланс - {self.value} {Account.suffix}')
#
#     def print_info(self):
#         print('Информация о счете')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}\nОстаток {self.value} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} успешно снято.\nОстаток {self.value} {Account.suffix}')
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} успешно зачислены\nТекущий баланс: {self.value} {Account.suffix}')
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def get_num(self):
#         return self.num
#
#     def set_num(self,num):
#         self.num = num
#
#     def get_surname(self):
#         return self.surname
#
#     def set_surname(self, surname):
#         self.surname = surname
#
#     def get_percent(self):
#         return self.percent
#
#     def set_percent(self, percent):
#         self.percent = percent
#
#     def get_value(self):
#         return self.value
#
#     def set_value(self, value):
#         self.value = value
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.set_num('asdgdg')
# print(acc.get_num())
# acc.set_surname('Ivanov')
# print(acc.get_num())
# acc.set_percent('0.07')
# print(acc.get_percent())
# acc.set_value('2000')
# print(acc.get_value())
# Задача 2_____________________________________________________________________________________________________________________________________________________________________________________
class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = 'RUB.'
    suffix_usd = 'USD.'
    suffix_eur = 'EUR.'

    def __init__(self, num, surname, percent, value=0):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f'Счет #{self.__num} принадлежащий {surname} был открыт.')
        print("*" * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счет #{self.__num} принадлежащий {self.surname} был закрыт')

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def edit_owner(self,surname):
        self.surname = surname

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print('Проценты были успешно начислены!')
        self.print_balance()

    def print_balance(self):
        print(f'Текущий баланс - {self.__value} {Account.suffix}')

    def print_info(self):
        print('Информация о счете')
        print('-' * 20)
        print(f'#{self.__num}')
        print(f'Владелец: {self.surname}')
        self.print_balance()
        print(f'Проценты: {self.__percent:.0%}')
        print('-' * 20)

    def withdraw_money(self, val):
        if val > self.__value:
            print(f'К сожалению у вас нет {val} {Account.suffix}\nОстаток {self.__value} {Account.suffix}')
        else:
            self.__value -= val
            print(f'{val} {Account.suffix} успешно снято.\nОстаток {self.__value} {Account.suffix}')

    def add_money(self, val):
        self.__value += val
        print(f'{val} {Account.suffix} успешно зачислены\nТекущий баланс: {self.__value} {Account.suffix}')

    @staticmethod
    def convert(value, rate):
        return value * rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f'Состояние счета: {eur_val} {Account.suffix_eur}')

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self,num):
        self.__num = num

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, percent):
        self.__percent = percent

    @property
    def value(self):
        return self.__percent

    @value.setter
    def value(self,percent):
        self.__percent = percent


acc = Account('123456', 'Долгих', 0.03, 1000)
acc.num = '12345ad'
acc.surname='Иванов'
acc.percent = 0.07
acc.value = 100
print(acc.num)
print(acc.value)
print(acc.surname)
print(acc.percent)

