unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print(f'\nVerifying users:{current_users.title()}')
    confirmed_users.append(current_users)

print(f'Following users have been confirmed:\n')
for confirmed_user in confirmed_users:
    print(f'\t{confirmed_user}')