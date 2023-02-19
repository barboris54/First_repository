people_in_poll = ['Zin','Tom','Max','Alex','Tom','Boris','Zin']
people_in_poll_1 = []
for humam in people_in_poll:
    if humam not in people_in_poll_1:
        people_in_poll_1.append(humam)
        print(f"{humam},would you like to take part in poll?")
    else:
        print(f'{humam} thank you')






