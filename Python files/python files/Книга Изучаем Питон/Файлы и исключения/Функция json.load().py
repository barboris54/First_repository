import json

filename = 'numbers.json'
with open(filename) as f:
    neumbers = json.load(f)

    print(neumbers)
