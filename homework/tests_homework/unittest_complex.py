import unittest
from unittest import mock
import tests_complex


class TestComplex(unittest.TestCase):

    def setUp(self) -> None:
        self.test = tests_complex.new_test()

    def tearDown(self) -> None:
        ok = self.defaultTestResult().wasSuccessful()
        if ok:
            print(f"test {self._testMethodName} Was Successful : {self.defaultTestResult().wasSuccessful()}")

    def test_hello(self):
        self.assertEqual(self.test.hello(), 1)

    @mock.patch('tests_complex.Test.hello', return_value=2)
    def test_hello_2(self, test):
        self.assertEqual(self.test.hello(), 2)

    def test_new_test(self):
        self.assertIsInstance(tests_complex.new_test(), tests_complex.Test)

    def test_func(self):
        self.assertEqual(self.test.hello(), 1)


if __name__ == '__main__':
    unittest.main()
