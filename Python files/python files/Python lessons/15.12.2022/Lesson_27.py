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
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner('Дюма')
# acc.print_info()
# acc.add_percents()
# print()
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(5000)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)

import re


class UserData:
    def __init__(self, fio, age, password, weight):
        # self.verify_fio(fio)
        # self.virify_old(age)
        # self.verify_weight(weight)
        # self.verify_ps(password)

        self.fio = fio
        self.age = age
        self.password = password
        self.weight = weight

    @staticmethod
    def verify_fio(fio):
        if not isinstance(fio, str):
            raise TypeError('ФИО должно быть строкой')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат ФИО')

        letter = "".join(re.findall('[a-zа-яё-]', fio, flags=re.I))
        for s in f:
            if len(s.strip(letter)) != 0:
                raise TypeError('В ФИО можно использовать только буквы или дефис')

    @staticmethod
    def virify_old(old):
        if not isinstance(old, int) or not 14 < old < 120:
            raise TypeError('возраст должен быть в заданом диапозоне')

    @staticmethod
    def verify_weight(w):
        if not isinstance(w, float) or w < 20:
            raise TypeError('Вес должен быть вещественным числом от 20 кг')

    @staticmethod
    def verify_ps(ps):
        if not isinstance(ps, str):
            raise TypeError('Паспорт должен быть строкой')
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Неверный формат паспорта')
        for p in s:
            if not p.isdigit():
                raise TypeError('Серия и номер должны быть цифрами')

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.virify_old(age)
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.verify_ps(password)
        self.__password = password


p1 = UserData('Волков Игорь Николаевич', 77, '1234 567890', 25.8)
p1.fio = 'Сидоров Игорь Николаевич'
print(p1.fio)