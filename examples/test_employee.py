import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('Davis', 'Tumuhaise', 5000000)
        self.emp_2 = Employee('Vicky', 'Nama', 3000000)

    def tearDown(self):
        pass 

    def test_email(self):
       

        self.assertEqual(self.emp_1.email, 'Davis.Tumuhaise@email.com')
        self.assertEqual(self.emp_2.email, 'Vicky.Nama@email.com')

        self.emp_1.first = 'Denis'
        self.emp_2.first = 'Dan'

        self.assertEqual(self.emp_1.email, 'Denis.Tumuhaise@email.com')
        self.assertEqual(self.emp_2.email, 'Dan.Nama@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Davis Tumuhaise')
        self.assertEqual(self.emp_2.fullname, 'Vicky Nama')

        self.emp_1.first = 'Denis'
        self.emp_2.first = 'Dan'

        self.assertEqual(self.emp_1.fullname, 'Denis Tumuhaise')
        self.assertEqual(self.emp_2.fullname, 'Dan Nama')

    

    if __name__ == '__main__':
        unittest.main()