numbers = [-2, 3, 8, -11, -4, 6]

def count(lst):
    cnt = 0
    if len(lst) == 1:
        return cnt
    if lst[0] < 0:
        cnt += 1
    else:
        cnt += count(lst[1:])
    return cnt
print(count(numbers))



