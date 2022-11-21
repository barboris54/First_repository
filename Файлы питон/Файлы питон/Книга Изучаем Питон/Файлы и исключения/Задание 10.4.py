active = True
while active:

    filename = 'guest_book.txt'
    guest_book = input('Enter your name')
    if guest_book.strip() == 'q':
        active = False
    else:
        with open(filename,'a') as file:
            file.write(f'{guest_book}\n')
            print(f'Hello {guest_book}')
