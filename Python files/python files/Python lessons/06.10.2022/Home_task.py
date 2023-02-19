# Задание № 1

# def find_max(lst):
#     max_elem = 0
#     for i in lst:
#         if i % 13 == 0:
#             max_elem = i
#     if max_elem > 0:
#         return max_elem
#     else:
#         return 'No Such number'
# lst = [int(input('->')) for i in range(int(input('введите количество символов')))]
# print(find_max(lst))

# Задание № 2
#
# tpl = (('ab','abcd','cde','abc','def'))
# def find_str(tpl):
#         index = tpl.index('ab')
#         return (tpl[index])
# if find_str(('ab','abcd','cde','abc','def')):
#     print(tpl)
#     print('Yes')
# else:
#     print('NO')

# Задание № 3

number = int(input('введите целое число '))
lst = list(str(number))
spare_list = []
for i in lst:
    if i not in spare_list:
        spare_list.append(i)
        print(f'Количество {i} = {lst.count(i)}')
    else:
        continue