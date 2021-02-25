import unittest
import test_simple_calc


class TestMod(unittest.TestCase):

    def test_add(self):
        self.assertEqual(test_simple_calc.add(4, 5), 9)
        self.assertEqual(test_simple_calc.add(3.9, 7.1), 11)
        self.assertEqual(test_simple_calc.add(-15, 3), -12)

    def test_substract(self):
        self.assertEqual(test_simple_calc.subtract(100, 28), 72)
        self.assertEqual(test_simple_calc.subtract(-35, 97), -132)
        self.assertEqual(test_simple_calc.subtract(990.001, 38.152), 951.8489999999999)

    def test_multiply(self):
        self.assertEqual(test_simple_calc.multiply(9, 9), 81)
        self.assertEqual(test_simple_calc.multiply(-25, 36), -900)
        self.assertEqual(test_simple_calc.multiply(5.5, 4.4), 24.200000000000003)

    def test_devide(self):
        self.assertEqual(test_simple_calc.divide(1, 1), 1)
        self.assertEqual(test_simple_calc.divide(x=5, y=2), 2.5)
        with self.assertRaises(ValueError):
            test_simple_calc.divide(1, 0)
        self.assertRaises(ValueError, lambda: test_simple_calc.divide(2, 0))


if __name__ == '__main__':
    unittest.main()
