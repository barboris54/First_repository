# Однако вторые имена нужны не всегда, а в такой записи функция не будет работать,
# если при вызове ей передается только имя и фамилия. Чтобы средний аргумент
# был необязательным, можно присвоить аргументу middle_name пустое значение по
# умолчанию; этот аргумент игнорируется, если пользователь не передал для него
# значение. Чтобы функция get_formatted_name() работала без второго имени, следует назначить для параметра middle_name пустую строку значением по умолчанию
# и переместить его в конец списка параметров:

def get_formated_name(firsr_name, lasr_name, middle_name=''):
    if middle_name:
        full_name = f'{firsr_name} {middle_name} {lasr_name}'
    else:
        full_name = f'{firsr_name} {lasr_name}'
    return full_name.title()


musician = get_formated_name('jimmy', 'hedrix')
musician_1 = get_formated_name('john', 'hooker', 'lee')
print(musician)
print(musician_1)
