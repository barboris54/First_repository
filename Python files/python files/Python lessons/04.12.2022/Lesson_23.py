file_name = 'res.txt'

# def longest_word(file):
#     with open(file, 'r', encoding='UTF-8') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         return res
#
#
# print(longest_word(file_name))

# text = 'Строка № 1\nСтрока № 2\nСтрока № 3\nСтрока № 4\nСтрока № 5\nСтрока № 6\nСтрока № 7\nСтрока № 8\nСтрока № 9\n'
#
# with open('one.txt','w',encoding='utf-8') as f:
#     f.write(text)
#
# read_file =  'one.txt'
# write_file = 'two.txt'
# with open(read_file,'r',encoding='utf-8') as fr, open(write_file,'w', encoding='utf-8') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'линия -')
#         fw.write(line)

# _____________________________________________________________________________________________________________________________________
# Модуль OS и OS.PATH

import os

# print('Текущая директория', os.getcwd())
#
# print(os.listdir()) # возвращает список директорий и файлов из текущей директории
# print(os.listdir('..'))
#
# os.mkdir('folder') # создает паку по указаному пути
# os.makedirs('nested/nested2/nested3') # создает несколько папок по указаному пути

# os.remove('one.txt') # удаляет файл

# os.rename('nested','test') # переименовывает файл или директорию

# os.rename('res.txt','test/res1.txt') # переменование + перенос файла в другую директорию

# os.rmdir('folder') # удлаяет только ПУСТУЮ директорию

# for root, dirs, files in  os.walk('test'): # возвращает имена объектов ввиде дерева директорий
#     # для каждой директории возвращает кортеж (путь к директории - root, список директорий - dir, спиок файлов - files)
#
#     print('Root:',root)
#     print('      Sumdirs',dirs)
#     print('             Files-',files)

# def remove_empty_dirs(root_tree):
#     for root, dirs, files in os.walk(root_tree):
#         print(root)
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория {root} удалена')
#
# remove_empty_dirs('test')
#
# print(os.path.split(r'D:\pythonProject\Файлы питон\Файлы питон\Python занятия\04.12.2022\Lesson_23.py')) # разбивает путь на картеж (head, tail)
#
# print(os.path.dirname(r'D:\pythonProject\Файлы питон\Файлы питон\Python занятия\04.12.2022\Lesson_23.py')) # возвращает путь к директории
#
# print(os.path.basename(r'D:\pythonProject\Файлы питон\Файлы питон\Python занятия\04.12.2022\Lesson_23.py')) # возвращает имя файла
#
# print(os.path.join(r'D:\pythonProject','Файлы питон','Файлы питон','Python занятия','04.12.2022','Lesson_23.py'))

# dirs = ['Work/F1', 'Work/F2/F21']
# for d in dirs:
#     os.makedirs(d)

# files = {'Work': ['w.txt'],
#          'Work/F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#          'Work/F2/F21': ['f211.txt', 'f212.txt']
#          }
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         open(file_path,'w').close()

file_text = ['Work/w.txt','Work/F1/f12.txt','Work/F2/F21/f211.txt','Work/F2/F21/f212.txt']
for file in file_text:
    with open(file,'w') as f:
        f.write(f'Text for file {file}')
