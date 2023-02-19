filename = 'guest.txt'
guest_name = input('Enter your name')
with open(filename,'w') as file:
    file.write(guest_name.strip())