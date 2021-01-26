import unittest


def division(a, b):
    return a // b


class TestDivision(unittest.TestCase):

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError) as e:
            division(5, 0)
