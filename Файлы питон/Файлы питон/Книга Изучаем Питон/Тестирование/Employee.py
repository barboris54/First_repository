class Employee():
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.salary = 5000

    def give_rise(self,rise = 5000):
        self.salary += rise

    def show_salary(self):
        print(f'{self.first.title()} {self.last.title()} earn {self.salary} anualy.')


emp = Employee('boris','borodin')
emp.give_rise(7000)
emp.show_salary()
