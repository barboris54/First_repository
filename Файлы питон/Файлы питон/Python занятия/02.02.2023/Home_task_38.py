import csv

with open('data2.csv', 'r', encoding='utf-8') as f:
    headers = ['hostname', 'vender', 'model','location']
    reader = csv.reader(f, delimiter=';')

    for i in reader:
        print(i)
