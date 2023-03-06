# from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

# name = 'Игорь'
# age = 28

# per = {'name':'igor','age':28}

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# per = Person('Игорь', 26)
#
# tm = Template('Мне {{ p.age }} лет. Меня зовут {{ p["name"] }}. ')
# msg = tm.render(p=per)
#
# print(msg)

# cities = [
# #     {'id':1, 'city':'Moscow'},
# #     {'id':2, 'city':'Smolensk'},
# #     {'id':3, 'city':'Minsk'},
# #     {'id':4, 'city':'Yaroslavl'},
# #     {'id':5, 'city':'Ufa'}
# # ]
# #
# # link = """<select name='cities'>
# # {% for c in cities %}
# # {% if c.id >3 -%}
# #     <option value="{{c['id'] }}>{{ c['city'] }}</option>
# # {% else %}
# #     {{c['city']}}
# # {% endif %}
# # {% endfor %}
# # </select>"""
# #
# # tm = Template(link)
# # msg = tm.render(cities=cities)
# #
# # print(msg)

# menu = [
#     {'href': '/index', 'name': 'Главная'},
#     {'href': '/news', 'name': 'Новости'},
#     {'href': '/about', 'name': 'О нас'},
#     {'href': '/shop', 'name': 'Магазин'},
#     {'href': '/contacts', 'name': 'Контакты'}
# ]
#
# link = """<ul>
#         {% for m in menu %}
#         {% if m.name == 'Главная'%}
#         <li><a href={{m.href}} class ='activ'></a>{{m.name}}</li>
#         {% else %}
#         <li><a href={{m.href}}></a>{{m.name}}</li>
#         {% endif %}
#         {% endfor %}
# </ul>"""
#
# tm = Template(link)
# msg = tm.render(menu=menu)
#
# print(msg)

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44300},
#     {'model': 'Wolksvagen', 'price': 21300}
# ]
#
# tp1 = 'Суммарная цена автомобилей {{ cs | sum(attribute="price") }}' # считает сумму стоиомсти автомобилей
# tm = Template(tp1)
# msg = tm.render(cs=cars)
#
# print(msg)

# html = """
# {% macro input(name, value='', type='text', size=20) %}
#     <input type='{{ type }}' name ='{{ name }}' value='{{ value }}' size='{{ size }}'>
# {% endmacro %}
#
# <p>{{ input('username', 'Ann') }}</p>
# <p>{{ input('email') }}</p>
# <p>{{ input('password', type='password') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)

# html = """
# {% macro input(name, placeholder='', type='text') %}
#     <input type='{{ type }}' name ='{{ name }}' placeholder='{{ placeholder }}'>
# {% endmacro %}
#
# <p>{{ input('firstname', 'Имя') }}</p>
# <p>{{ input('lastname','Фамилия') }}</p>
# <p>{{ input('adress', 'Адресс') }}</p>
# <p>{{ input('phone', type='tel', placeholder='Телефон') }}</p>
# <p>{{ input('email', 'Почта','email') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)

# persons = [{"name": "Алексей", "year": 18, "weight": 78.5},
#            {"name": "Никита", "year": 28, "weight": 82.3},
#            {"name": "Виталий", "year": 33, "weight": 94.0}
#            ]
#
# html = """
# {% macro list_users(list_of_users) %}
# <ul>
# {% for u in list_of_users %}
#     <li>{{ u.name }} {{ caller(u) }}</li>
# {% endfor%}
# </ul>
# {% endmacro %}
#
# {% call(user) list_users(users) %}
#     <ul>
#         <li>{{ user.year }}</li>
#         </li>{{ user.weight }}</li>
#     </ul>
# {% endcall %}
#
#
# """
#
# tm = Template(html)
# msg = tm.render(users=persons)
# print(msg)


# БЕРЕМ РАЗМЕТКУ ИЗ HTML__________________________________________________________________________________________________

persons = [
    {"name": "Алексей", "year": 18, "weight": 78.5},
    {"name": "Никита", "year": 28, "weight": 82.3},
    {"name": "Виталий", "year": 33, "weight": 94.0}
]

file_loader = FileSystemLoader('Tepmplates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(users=persons)

print(msg)
