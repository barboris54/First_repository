from survey import AnonymousSurvey

# Определение вопроса с созданием экземпляра
question = 'What is your favorite foreing language ?'
my_survey = AnonymousSurvey(question)

# Вывод пороса и сохрарнение ответа
my_survey.show_question()
print('Enter q at any time to quit\n')
while True:
    response = input('What is your favorite foreing langauge?')
    if response == 'q':
        break
    else:
        my_survey.store_response(response)


# вывод результатов опроса
print('Thanks for Everyone who take part in survey')
my_survey.show_result()