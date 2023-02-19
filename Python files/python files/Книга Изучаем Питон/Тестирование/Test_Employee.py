import unittest
from Employee import Employee
class TestEmployee(unittest.TestCase):

    def SetUp(self):
        self.emp = Employee('boris','borodin')
        self.salary = 5000

    def test_give_default_rise(self):
        salary = 5000
        self.emp.give_rise()
        self.assertEqual(salary,10000)

    def test_give_custom_rise(self):
        self.emp.give_rise(7000)
        self.assertEqual(self.emp.salary,12000)

if __name__ =='__main__':
    unittest.main()