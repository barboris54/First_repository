countries = ['russia','usa','germany','japan']
print(countries[0].title())
countries.pop(1)
print(countries)
countries.remove('japan')
print(countries)
countries.append('Canada')
print(countries)
countries.insert(3,'Italy')
print(countries)
countries[0]='England'
print(countries)
del (countries[2])
print(countries)
print(sorted(countries))
countries.sort()
print(countries)
countries.reverse()
print(countries)
print(len(countries))
