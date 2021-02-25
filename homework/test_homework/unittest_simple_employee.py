import unittest
from unittest.mock import patch

from tests_simple_employee import Employee

man = Employee('Clark', 'Jonson', 35000)
woman = Employee('Jenifer', 'Anderson', 99999)


class TestEmployee(unittest.TestCase):

    def test_email(self):
        self.assertEqual(man.email, 'Clark.Jonson@email.com')
        self.assertEqual(woman.email, 'Jenifer.Anderson@email.com')
        woman.last = 'Wayne'
        self.assertEqual(woman.email, 'Jenifer.Wayne@email.com')

    def test_fullname(self):
        man.first = 'Bruce'
        self.assertIsNot(man.fullname, 'Bruce Jonson')
        self.assertEqual(woman.fullname, 'Jenifer Wayne')

    def test_apply_raise(self):
        man = Employee('john', 'Solomon', 50000)
        man.apply_raise()
        self.assertEqual(man.pay, 52500)
        woman.apply_raise()
        self.assertEqual(woman.pay, 104998)

    def test_monthly_schedule(self):
        with patch('tests_simple_employee.requests.get') as mock:
            mock.return_value.ok = False
            mock.return_value.text = 'Done'

            person = Employee('Ivan','Lyniv', 20000)
            schedule = person.monthly_schedule('January')
            mock.assert_called_with("http://company.com/Lyniv/January")
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
