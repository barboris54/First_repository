class Power:
    def __init__(self, mul):
        self.mul = mul

    def __call__(self, fn):
        def wrap(a, b):
            print('Result:', (a + b) ** self.mul)

        return wrap


@Power(3)
def multiply(a, b):
    return a * b


multiply(2, 2)
