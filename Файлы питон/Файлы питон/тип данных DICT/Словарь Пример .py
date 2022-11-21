person = {}
s = "IVANOV IVAN Samara SGU 4 5 5 3 4 4"
s = s.split()
print(s)
person['LastName'] = s[0]
person['FirstName'] = s[1]
person['university'] = s[3]
person['marks'] = []
for i in s[4:]:
    person['marks'].append(int(i))
print(s)
print(person)
