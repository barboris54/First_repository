s = 'заменить в этой строке все все появления буквы "о" на "О" кроме первого и последнего вхождения'
first= s.find('о')
last = s.rfind('о')
print(s)
new = s[first+1:last]
new_1 = new.replace('о','О')
print(s[:first+1] + new_1 + s[last:])
