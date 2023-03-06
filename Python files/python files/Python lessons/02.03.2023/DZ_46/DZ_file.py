from jinja2 import Environment, FileSystemLoader



p = ['страница с домашним задание № 1',
    'страница с домашним задание № 2',
    'страница с домашним задание № 3',
     ]

file_loader = FileSystemLoader('Templates1')
env = Environment(loader=file_loader)

tm = env.get_template('main1.html')
msg = tm.render(pages=p)
print(msg)