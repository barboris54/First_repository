favorite_numbers = {'bob': [1, 4, 6],
                    'tom': [12, 7, 2],
                    'jack': [44]
                    }
for name, digits in favorite_numbers.items():
    if len(digits) == 1:
        print(f'{name} likes only digit:')
        for digit in digits:
            print(digit)
    else:
        print(f'{name}s fovorite digits are:')
        for digit in digits:
            print(digit)
