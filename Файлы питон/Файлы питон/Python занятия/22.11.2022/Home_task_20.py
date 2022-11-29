# Задание № 1
import re

# str = '1X, TEXT ABC 123 A1B2C3'
# pattern = r'\D(\d)'
# print(re.findall(pattern,str))

# Задание № 2

# text = 'text from #START# till #END#'
# pattern = r'#(\s\w+\s)#'
# print(re.findall(pattern,text))

# Задание № 3

text = '12_34__56'
pattern = r'(\d+)_[^_]'
print(re.findall(pattern,text))

