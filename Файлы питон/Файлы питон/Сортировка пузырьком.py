n = 6
a = [5,7,4,3,8,2]
count = 0
for run in range(n-1):
    for i in range(n-1-run):
        if a[i] > a[i+1]:
            count += 1
            a[i], a[i+1] = a[i+1], a[i]
print(*a)
print(count)