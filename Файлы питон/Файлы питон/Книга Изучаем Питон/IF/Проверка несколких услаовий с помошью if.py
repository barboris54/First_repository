# иногда бывает важно проверить все условия, представляющие интерес.
# В таких случаях следует применять серии простых команд if без блоков elif или else
# Такое решение уместно, когда истинными могут быть сразу несколько условий и вы хотите отреагировать на все истинные.

requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'peperoni' in requested_toppings:
    print('Adding peproni')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')

# Итак, если вы хотите, чтобы в программе выполнялся только один блок кода, используйте цепочку if-elif-else. Если же выполняться должны несколько блоков,
# используйте серию независимых команд if