import json

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        a = ''
        for i in self.marks:
            a += f'{i},'

        return f'Студкет: {self.name} {a[:-1]}'

    def add_marks(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        self.marks.pop(index)

    def change_mark(self, index, new_mark):
        self.marks[index] = new_mark

    def avarage_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    @staticmethod
    def dump_to_json(stud, filename):
        try:
            data = json.load(open(filename))
        except FileNotFoundError:
            data = []
        data.append({'name': stud.name, "marks": stud.marks})
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'r') as f:
            print(json.load(f))


class Group:
    def __init__(self, students, group):
        self.students = students
        self.group = group

    def __str__(self):
        a = ''
        for i in self.students:
            a += str(i) + '\n'
        return f'Группа:{self.group}\n{a}'

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    @staticmethod
    def change_group(group1, group2, index):
        return group2.add_student(group1.remove_student(index))

    @staticmethod
    def dump_group(file, group):
        try:
            data = json.load(open(file))
        except FileNotFoundError:
            data = []

        with open(file, 'w') as f:
            stud_list = []
            for i in group.students:
                stud_list.append([i.name, i.marks])
            data.append(stud_list)
            json.dump(data,f, indent=2)

    @staticmethod
    def upload_journal(file):
        with open(file, 'r') as f:
            print(json.load(f))




st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
st2 = Student('Nikolaenko', [2, 3, 4, 5, 2, 4])
sts = [st1,st2]
my_group = Group(sts, 'Web')
# print(st1)
# Student.dump_to_json(st1, 'student.json')
# Student.load_from_file('student.json')

# Student.dump_to_json(st2, 'student.json')
# Student.load_from_file('student.json')
Group.dump_group('group.json', my_group)
Group.upload_journal('group.json')