def make_album(name,album,count_rt=None):

    info_album = {'person':name, 'favorite_album': album}
    if count_rt:
        info_album['count_tr']= count_rt
    return info_album


active = True
while active:
    person_name = input('Enter your name').strip()
    if person_name == 'q':
        break
    person_album = input('Enter your favorite album').strip()
    if person_album == 'q':
        break
    my_fovorite_album= make_album(person_name,person_album,)
    print(my_fovorite_album)