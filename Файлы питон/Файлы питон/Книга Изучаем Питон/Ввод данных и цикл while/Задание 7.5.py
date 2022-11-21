message = 'How old are you ?'

activ = True
while activ:
    age = int(input(message).strip())
    if age < 3:
        print('You can visit movie for free')
    if 3 < age < 12:
        print('Ticket costs 10$')
    if age > 12:
        print('Ticket costs is 15$')
    activ = False