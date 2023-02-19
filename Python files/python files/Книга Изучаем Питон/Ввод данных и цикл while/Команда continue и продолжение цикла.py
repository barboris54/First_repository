# Вместо того чтобы полностью прерывать цикл без выполнения оставшейся части
# кода, вы можете воспользоваться командой continue для возвращения к началу
# Циклы while 137
# цикла и проверке условия

current_number = 0
while current_number <10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)

