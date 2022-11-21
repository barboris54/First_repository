import re
password = 'my-p@ssw0rd1_'
pattern = r'[0-9A-z@\-_$]{6,18}'
s = re.findall(pattern, password)
if s[0] == password:
    print(s)
else:
    print('Невалидный пароль')
