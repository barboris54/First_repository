current_users = ['mike', 'bob', 'john', 'bill', 'mark']
new_users = ['tom', 'jim', 'bob', 'john', 'tim']
for user in new_users:
    if user.lower() in current_users:
        print(f'Name {user.title()} alreay used')
    else:
        print(f'Name {user.title()} is aviable')
