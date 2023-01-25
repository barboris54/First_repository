class Verify:
    def __init__(self,a,b,c):
        if not isinstance(a, int) and not isinstance(b, int) and not isinstance(c, int):
            raise ValueError
        else:
            self.a = a
            self.b = b
            self.c = c
    def __call__(self):
        if self.a < 0 or self.b < 0 or self.c < 0:
            raise ValueError


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def exist(self):
        if ((self.a + self.b) > self.c) and ((self.b + self.c) > self.a) and ((self.a + self.c) > self.b):
            return True
        else:
            return False


