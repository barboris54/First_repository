responses = {}

poll_active = True
while poll_active:
    name = input('What is your name?').strip()
    responce =input('What is your favorite colour').strip()

    responses[name] = responce

    repeat = input('Would you like to let another person to response ??  yes/no')
    if repeat.strip() == 'no':
        poll_active = False

for name,response in responses.items():
    print(f"{name.title()}'s favorite colours is {response.title()}")