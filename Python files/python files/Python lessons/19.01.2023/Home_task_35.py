class Verify:
   @staticmethod
   def verify(a):
       if not isinstance(a,int) or a < 0:
           raise TypeError(f'Координата {a} должга быть целым полодительным числом')

   def __set_name__(self, owner, name):
       self.name = '_' + name

   def __get__(self, instance, owner):
       return getattr(instance, self.name)

   def __set__(self, instance, value):
       self.verify(value)
       setattr(instance,self.name, value)

class Triangle:

    a = Verify()
    b = Verify()
    c = Verify()
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def exist(self):
        if ((self.a + self.b) > self.c) and ((self.b + self.c) > self.a) and ((self.a + self.c) > self.b):
            return True
        else:
            return False


tr1 = Triangle(5,2,5)
print(tr1.exist())
print(tr1.__dict__)