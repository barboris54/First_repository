def build_profile(first,last,**kwargs):
    kwargs['first_name'] = first.title()
    kwargs['last_name'] = last.title()
    return kwargs
my_profile = build_profile('boris','borodin',country = 'Russia',city = 'Rostov')

for info,me in my_profile.items():
    print(info,me)

