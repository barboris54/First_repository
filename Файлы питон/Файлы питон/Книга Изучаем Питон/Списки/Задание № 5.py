People = ['Abraham Linkoln', 'Papich', 'Nikola Tesla']
People.insert(0, 'Dima')
People.insert(2, 'Alex')
People.insert(5, 'Ivan')
print(People)
new_comers_1 = People[0]
new_comers_2 = People[2]
new_comers_3 = People[5]

print(f'I decide to extend our party and invite:\t\n{new_comers_1}\t\n{new_comers_2}\t\n{new_comers_3}')

for i in People:
    print(i, 'We are waitnig for you')
print('Fianally I waiting for', len(People),'people')
