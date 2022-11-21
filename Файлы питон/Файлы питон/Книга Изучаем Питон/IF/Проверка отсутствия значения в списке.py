# В других случаях программа должна убедиться в том, что значение не входит
# в список. Для этого используется ключевое слово not.

banned_users = ['andrew','alex','tom']
user = 'max'
if user not in banned_users:
    print(f'{user.title()} you can post your respond on the wall !')