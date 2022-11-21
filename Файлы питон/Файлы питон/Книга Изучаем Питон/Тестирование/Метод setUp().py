import unittest
from survey import AnonymousSurvey

# Класс unittest.TestCase содержит метод
# setUp(), который позволяет создать эти объекты один раз, а затем использовать их
# в каждом из тестовых методов. Если в класс TestCase включается метод setUp(),
# Python выполняет метод setUp() перед запуском каждого метода, имя которого начинается с test_. Все объекты, созданные методом setUp(), становятся доступными
# во всех написанных вами тестовых методах.

class TestAnonymousSurvey(unittest.TestCase):
    """Тест для класса AnonymousSurvey """

    def SetUp(self):
        """Создание опроса и ответа для всех тестовых модулей"""

        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):

        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)



if __name__ =='__main__':
    unittest.main()