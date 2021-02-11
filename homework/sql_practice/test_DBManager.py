import unittest
from DBManager import DBManager
import psycopg2
import datetime


class TestPositiveDBManager(unittest.TestCase):

    def setUp(self) -> None:
        self.testdb = DBManager()

    def tearDown(self) -> None:
        self.testdb.commit_db()
        self.testdb.close_cursor()
        self.testdb.connection_close()
        ok = self.defaultTestResult().wasSuccessful()
        if ok:
            print(f"test {self._testMethodName} Was Successful : {self.defaultTestResult().wasSuccessful()}")

    def test_user(self):
        create_user = self.testdb.create_user(
            {'name': 'Katya', 'email': 'katya@ukr.net', 'registration_time': '2021-02-05 14:32:27'})
        self.assertEqual(create_user, self.testdb.read_user_info(4))

        update_user = self.testdb.update_user({'name': 'Roman', 'email': 'roman@gmail.com'}, 4)
        self.assertEqual(update_user, self.testdb.read_user_info(4))

        self.testdb.delete_user(4)
        self.assertEqual(self.testdb.read_user_info(4), None)

    def test_cart(self):
        create_cart = self.testdb.create_cart({'creation_time': '2021-02-04 17:40:59', 'user_id': '3'})
        self.assertEqual(create_cart, self.testdb.read_cart(5))

        update_cart = self.testdb.update_cart({'creation_time': '2021-02-05 16:59:00', 'user_id': '3'})
        self.assertEqual(update_cart, self.testdb.read_cart(4))

        self.testdb.delete_cart(4)
        self.assertEqual(self.testdb.read_cart(4), None)


class TestNegativeDBManager(unittest.TestCase):

    def setUp(self) -> None:
        self.testdb = DBManager()

    def tearDown(self) -> None:
        self.testdb.commit_db()
        self.testdb.close_cursor()
        self.testdb.connection_close()
        ok = self.defaultTestResult().wasSuccessful()
        if ok:
            print(f"test {self._testMethodName} Was Successful : {self.defaultTestResult().wasSuccessful()}")

    def test_user(self):

        user = {'name': 'Roman', 'email': 'igor@gmail.www', 'registration_time': '2021'}

        self.assertRaises(psycopg2.Error, lambda: self.testdb.create_user(user))

        update_user = {'name': 'Petro', 'email': 'petro@org.ua'}
        self.testdb.update_user(update_user, 4)
        self.assertNotEqual(self.testdb.read_user_info(4), (4, 'Roman', 'romchuk@gmail.com', datetime.datetime(2021, 2, 4, 17, 40, 59)))

        self.testdb.delete_user(4)
        self.assertIsNone(self.testdb.read_user_info(4))

    def test_cart(self):
        cart = {'creation_time': '2021', 'user_id': '3'}
        self.assertRaises(psycopg2.Error, lambda: self.testdb.create_cart(cart))

        update_cart = {'creation_time': '2021-02-05 16:59:00', 'user_id': '3'}
        self.testdb.update_cart(update_cart)
        self.assertNotEqual(update_cart, (4, datetime.datetime(2021, 10, 11, 4, 0), 1))

        self.testdb.delete_cart(4)
        self.assertIsNone(self.testdb.delete_cart(4))


if __name__ == '__main__':
    unittest.main()
