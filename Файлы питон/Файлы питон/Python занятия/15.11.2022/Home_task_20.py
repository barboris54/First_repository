import re

a = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78'
pattern = r'(?:\+7|7)\s*\(?499\)?\s*\d{3}.?\d{2}.?\d{2}'
print(re.findall(pattern, a))
print('hello')