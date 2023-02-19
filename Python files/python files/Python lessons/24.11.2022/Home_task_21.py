# numbers = [-2, 3, 8, -11, -4, 6]
# cnt = 0
#
#
# def count(lst):
#     global cnt
#     if not lst:
#         return
#     else:
#         frs = lst[0]
#         if frs < 0:
#             cnt += 1
#         count(lst[1:])
#     return cnt
#
#
# print(count(numbers))

# Задание 2

names = ['Adam',['Bob',['Chet','Cat'],'Bard','Bert'],'Alex',['Bea','Bill'],'Ann']

def count_names(lst):
    count = 0
    for i in lst:
        if isinstance(i,list):
            for q in i:
                if isinstance(q, list):
                    for a in q:
                        count += 1
                else:
                    count += 1
        else:
            count += 1
    return count

print(count_names(names))
