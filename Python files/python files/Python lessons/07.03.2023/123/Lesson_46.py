from jinja2 import Environment, FileSystemLoader

# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.3},
#     {"name": "Виталий", "year": 33, "weight": 94.0}
# ]

subs = ['культура', 'Наука', 'Политика ', 'Спорт' ]

file_loader = FileSystemLoader('Tepmplates2')
env = Environment(loader=file_loader)

tm = env.get_template('about.html')
msg = tm.render(list_table=subs)

print(msg)
