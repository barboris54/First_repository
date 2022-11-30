# f = open('text.txt', 'r')
# print(f)
# print(*f)
# print(f.closed)
#
# f = open('text.txt', 'r')
# print(f.read())
# f.close()

# f = open('text.txt', 'r')
# try:
#     print(f.read()
# finally:
#     f.close()

# f = open('test.txt','r')
# print(f.readlines())
# f.close()

# f = open('test.txt','r')
# count = 0
# for line in f:
#     count += 1
# f.close()
# print(count)

# f = open('xyz.txt', 'w')
# f.write('Hello\nпарапрпа')
# f.close()

# f = open('xyz.txt', 'a', encoding='UTF-8')
# # f.write('\nNew text')
# lines = ['\nЛиния 1', '\nЛиния 2']
# f.writelines(lines)
# f.close()

# f = open('xyz.txt','w')
# lst = [str(i) + str(i-1) + '\t'  for i in range(1,20)]
# print(lst)
# f.writelines(lst)
# f.close()

# f = open('text2.txt','w')
# f.write('Замена строки в текстовом файле;\nизмнеить строку в списке;\nзаписать список в файл')
# f.close()
#
# f = open('text2.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == 'измнеить строку в списке;\n':
#         read_file[i] = 'hello world !\n'
# print(read_file)
# f.close()
#
# f = open('text2.txt','w')
# f.writelines(read_file)
#
# f = open('text2.txt','w')
# f.write('Замена строки в текстовом файле;\nизмнеить строку в списке;\nзаписать список в файл')
# f.close()
#
# f = open('text2.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# line_del = int(input('номер строки'))
# for i in range(len(read_file)):
#     if len(read_file) < line_del - 1:
#         print('Нет такой строки')
#     else:
#         read_file.pop(line_del - 1)
#         print(read_file)
# f.close()
#
# f = open('text2.txt','w')
# f.writelines(read_file)
# f.close()

# f = open('text3.txt', 'w')
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# f.close()
#
#
# f = open('text3.txt', 'r')
# read_line = f.readlines()
# print(read_line)
# n = int(input("Введите индекс: "))
# if 0 <= n < len(read_line):
#     read_line.pop(n)
# else:
#     print('Такой строки нет')
# print(read_line)
# f.close()
#
#
# f = open('text3.txt', 'w')
# f.writelines(read_line)
# f.close()

# f = open('text.txt','r')
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# f.close()


f = open('text.txt','r+')
print(f.write('I am learning Python'))
print(f.seek(3))
print(f.write('--new string--'))
print(f.tell())
f.close()