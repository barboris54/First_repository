class AnonymousSurvey():
    """Сбор анонимных ответов"""

    def __init__(self, question):
        """Сохроняет вопрос и готовится к сохранению ответов """
        self.question = question
        self.responses = []

    def show_question(self):
        """Выводит вопрос"""
        print(self.question)

    def store_response(self, new_response):
        """Сохраняет один ответ"""
        self.responses.append(new_response)

    def show_result(self):
        """Выводит все ответы"""
        print('Survey result:')
        for response in self.responses:
            print(f'- {response}')




