class Student:
    def __init__(self,name):
        self.name = name
        self.lp = self.Laptop('HP','i7','8')


    def show_info(self):
        print(f'{self.name} => {self.lp.core}, {self.lp.model}, {self.lp.ram}')

    class Laptop:
        def __init__(self,model, core, ram):
            self.model = model
            self.core = core
            self.ram = ram


student = Student('Vladimir')
student.show_info()
student2 = Student('Roman')
student2.show_info()