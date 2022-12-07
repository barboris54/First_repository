# Задание 1
result_file = 'Res_file.txt'
read_file_1 = 'File_1.txt'
read_file_2 = 'File_2.txt'
with open(result_file,'a') as rf, open(read_file_1,'r') as f1, open(read_file_2,'r') as f2:
    words = f1.read()
    words_2 = f2.read()
    rf.write(words)
    rf.write(words_2)

# Задание 2
#
# file_text = ['Work/w.txt','Work/F1/f12.txt','Work/F2/F21/f211.txt','Work/F2/F21/f212.txt']
#
# def tree(root,a):
#     print(f'Обход репозитория {root} {"сверху вниз" if a else "снизу вверх"}')
#     for root, dirs, files in os.walk(root, topdown=a):
#         print(root)
#         print(dirs)
#         print(files)
#
#
#
# tree('Work',topdown=False)
# tree('Work',topdown=True)