import unittest
from city_function import country_city

class TestCities(unittest.TestCase):
    """возвращает ли функия сообщение типо Страна,Город"""

    def test_country_city(self):
        formated_message = country_city('russia','moskow')
        self.assertEqual(formated_message,'Russia, Moskow')

    def test_country_city_poplation(self):
        """Возвращает ли функция сообщения типа Страна,Город - население"""
        formated_message = country_city('russia','moskow',10000000)
        self.assertEqual(formated_message,'Russia, Moskow - Population 10000000')
if __name__ == '__main__':
    unittest.main()