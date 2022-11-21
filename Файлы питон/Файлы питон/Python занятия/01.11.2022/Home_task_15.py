def binNum():
    num = int(input('-> '))
    bn = ''
    while num > 0:
        bn += str(num%2)
        num = num//2
    return bn
print(binNum())