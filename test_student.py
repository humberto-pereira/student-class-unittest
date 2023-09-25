import unittest
from student import Student

class TestSudent(unittest.TestCase):


    @classmethod
    def setUpClass(cls):  # add an instance Class at the beginning of all tests instead of the beginning of every single test used for the test database, for example (run to see the print output)
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):  # the same as setUp Class, but instead to add, it removes... and is called at the end of the test
        print('tearDownClass')


    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')  # add an instance passing self.student == ('John', 'Doe')

    def test_full_name(self):
        print('full_name')
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)
    
    def tearDown(self):
        print('tearDown')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, 'john.doe@email.com')


if __name__ == '__main__':
    unittest.main()