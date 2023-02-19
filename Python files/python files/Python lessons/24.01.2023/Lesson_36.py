import pickle
import json

# filename = 'basket.txt'
#
# shop_list = {
#     'овощи': ['яблоки', 'манго'],
#     'фрукты': ['морковь'],
#     'бюджет': 1000,
# }
#
# with open(filename, 'wb') as f:
#     pickle.dump(shop_list, f)
#
# with open(filename, 'rb') as f:
#     shop = pickle.load(f)
#
# print(shop)


# class Test:
#     num = 35
#     st = 'Hello'
#     lst = [1, 2, 3, 4]
#     d = {'1': 'a', '2': 2}
#     tpl = (22, 33)
#
#     def __str__(self):
#         return f'Num: {Test.num}\nСтрока: {Test.st}\nСловарь: {Test.d}\nСписок:{Test.lst}'
#
# obj = Test()
#
# my_obj = pickle.dumps(obj)
# print(my_obj)
#
# l_obj = pickle.loads(my_obj)
# print(l_obj)

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         # self.c = lambda x: x * x
#
#     def __str__(self):
#         return f'{self.a} {self.b}'
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)

data = {
    'name': 'Igor',
    'hobbies': ['running', 'sky diving'],
    'age': 20,
    'children': [
        {
            'firstName': 'Alice',
            'age': 5
        },
        {
            'firstName': 'Bob',
            'age': 8
        }
    ]
}

with open('data_file.json', 'w') as fw:
    json.dump(data, fw, indent=4)

with open('data_file.json', 'r') as fw:
    a = json.load(fw)

print(a)

json_string = json.dumps(data)

data = json.loads(json_string)
print(data)
