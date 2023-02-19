# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Name:',self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = 'Smith'
#             self.id = '657'
#
#         def display(self):
#             print('Name:', self.name)
#             print('Id:', self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#             self.id = '007'
#
#         def display(self):
#             print('Name:', self.name)
#             print('Id:', self.id)
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# print()
# d1.display()
# print()
# d2 = outer.head
# d2.display()

# class Computer:
#     def __init__(self, name, os1):
#         self.name = name
#         self.os = self.OS(os1)
#         self.cpu = self.CPU()
#
#     class OS:
#         def __init__(self, title):
#             self.title = title
#
#         def system(self):
#             return self.title
#
#     class CPU:
#         def make(self):
#             return 'Intel'
#
#         def model(self):
#             return 'core - i7'
#
#
# comp = Computer('PC001', 'Windows 7')
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.title)
# print(my_cpu.make())
# print(my_cpu.model())

# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def dispaly(self):
#         print('In Base Class')
#
#     class Inner:
#         def display1(self):
#             print('Inner of Base Class')
#
#
# class Subclass(Base):
#     def __init__(self):
#         print('In Subclass')
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print('Inner of SubClass')
#
# a = Subclass()
# a.dispaly()
#
# b = Subclass.Inner()
# b.display1()
# b.display2()

# Множественное наследование ___________________________________________________________________

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + 'is sleeping')
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + 'is playing')
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + 'is barking')
#
#
# beast = Dog('Buddy ')
# beast.bark()
# beast.play()
# beast.sleep()

# class A:
#     def __init__(self):
#         print('A')
#
#
# class B(A):
#     def __init__(self):
#         print('B')
#
#
# class C(A):
#     def __init__(self):
#         print('C')
#
#
# class D(B, C):
#     def __init__(self):
#         # super().__init__()
#         C.__init__(self)
#         B.__init__(self)
#         print('D')
#
#
# d = D()

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'{self.x}, {self.y}'
#
#
# class Style:
#     def __init__(self, color='red', width=1):
#         print('Инициализатор Style')
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point):
#         self._sp = sp
#         self._ep = ep
#
#
# class Line(Pos, Style):
#     def __init__(self, sp: Point, ep: Point, color='red', width=1):
#         Pos.__init__(self, sp, ep)
#         Style.__init__(self, color, width)
#
#     def draw(self):
#         print(f'Рисование линии: ({self._sp}), ({self._ep}), {self._color}, {self._width}')
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()

# Миксин (примеси) _______________________________________________________________

class Displayer:
    @staticmethod
    def display(message):
        print(message)


class LoggerMixin:
    def log(self, message, filename='logfile.txt'):
        with open(filename, 'w') as fh:
            fh.write(message)

    def disolay(self, message):
        Displayer.display(message)
        self.log(message)


class MycClass(LoggerMixin, Displayer):
    def log(self, message, filename=''):
        super().log(message, filename='subclasslog.txt')


sub = MycClass()
sub.display('Строка будет отображаться и регистрироваться в файле')
