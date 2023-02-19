def middle(fn):
    def inner(*args):
        print('Cреднее арифметическое чисел:', *args, '=', sum(args) / len(args))
        fn(*args)

    return inner


@middle
def summarize(*args):
    lst = list(args)
    print('Сумма чисел :', *args, '=', sum(lst))


(summarize(2, 3, 3, 4))
