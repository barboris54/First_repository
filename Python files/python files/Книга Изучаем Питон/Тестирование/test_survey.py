import unittest
from survey import AnonymousSurvey

# Напишем тест, проверяющий всего один аспект поведения AnonymousSurvey. Этот
# тест будет проверять, что один ответ на опрос сохраняется правильно. После того
# как метод будет сохранен, метод assertIn() проверяет, что он действительно находится в списке ответов:

class TestAnonymousSurvey(unittest.TestCase):
    """Тест для класса AnonymousSurvey """

    def test_single_response_store(self):
        """Проверяет, что один ответ сохранен правильно"""
        question = 'What is your favorite language ?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.response)

    def  test_three_resposnes_store(self):
        question = 'What is your favorite language ?'
        my_survey = AnonymousSurvey(question)
        responses = ['Russian','English','German']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response,my_survey.response)



if __name__ =='__main__':
    unittest.main()