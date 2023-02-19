import json
from random import choice


def get_person():
    name = ''
    tel = ''


    letter = ['a', 'b', 'c', 'd', 'e']
    nums = ['1', '2', '3', '4', '5', '6', '7']



    print(name)

    while len(name) != 7:
        name += choice(letter)

    print(name)

    while len(tel) != 10:
        tel += choice(nums)

    print(tel)

    dic = {
        'name': name,
        'tel': tel
    }
    return dic


def write_json(person_dict):
    dic = ''
    dic_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    while len(dic) != 7:
        dic += choice(dic_let)
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = {}

    data[dic] = person_dict
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(get_person())
