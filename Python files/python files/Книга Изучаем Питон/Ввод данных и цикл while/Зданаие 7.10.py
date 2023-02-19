poll_result = []
responder = {}

active = True
while active:
    name = input("what is your name ?")
    country = input("what country would you like to visit ?")

    responder[name] = country

    repeat = input('Would you like another person take part in poll yes/no ?').strip()
    if repeat == 'no':
        active = False
for name,country in responder.items():
    print(f'{name.title()} would like to visit {country.title()}\n')