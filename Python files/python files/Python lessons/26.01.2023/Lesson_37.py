# import json
# from random import choice
#
#
# def get_person():
#     name = ''
#     tel = ''
#
#     letter = ['a', 'b', 'c', 'd', 'e']
#     nums = ['1', '2', '3', '4', '5', '6', '7']
#
#     while len(name) != 7:
#         name += choice(letter)
#
#     print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     print(tel)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(get_person())

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


st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
st2 = Student('Nikolaenko', [2, 3, 4, 5, 2, 4])
st3 = Student('Birukov', [5, 5, 4, 2, 4, 3])
sts = [st1, st2]

my_group = Group(sts, 'ГК')

# print(st1)
# st1.add_marks(4)
# print(st1)
# st1.delete_mark(1)
# print(st1)
# print(st1.avarage_mark())
# print(my_group)
# my_group.add_student(st3)
print(my_group)
group22 = [st3]
my_group2 = Group(group22, 'Web')
print(my_group2)
Group.change_group(my_group, my_group2, 0)
print(my_group2)
