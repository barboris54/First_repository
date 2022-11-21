People = ['Abraham Linkoln', 'Papich', 'Nikola Tesla']
People.insert(0, 'Dima')
People.insert(2, 'Alex')
People.insert(5, 'Ivan')
print('Unfortunatelly I can invite only two people')
popped_people_1, popped_people_2, popped_people_3, popped_people_4 = People.pop(0), People.pop(1), People.pop(
    2), People.pop(2)
print(f'{popped_people_1}, unfortunatelly i cant invite you')
print(f'{popped_people_2}, unfortunatelly i cant invite you')
print(f'{popped_people_3}, unfortunatelly i cant invite you')
print(f'{popped_people_4}, unfortunatelly i cant invite you')
for i in People:
    print(i, 'I still waiting for you')
del People[0]
del People[0]
print(People)
