import unittest
from DBManager import DBManager
import pytest

class TESTDBManager(unittest.TestCase):

    def setUp(self) -> None:
        self.testdb = DBManager()

    def tearDown(self) -> None:
        ok = self.defaultTestResult().wasSuccessful()
        if ok:
            print(f"test {self._testMethodName} Was Successful : {self.defaultTestResult().wasSuccessful()}")

    def close_session_db(self):
        """commit and close connection with database"""
        self.testdb.commit_db()
        self.testdb.close_cursor()
        self.testdb.connection_close()

    def test_user(self):
        create_user = self.testdb.create_user(
            {'name': 'Katya', 'email': 'katya@ukr.net', 'registration_time': '2021-02-05 14:32:27'})
        self.assertEqual(create_user, self.testdb.read_user_info(4))

        update_user = self.testdb.update_user({'name': 'Roman', 'email': 'roman@gmail.com'}, 4)
        self.assertEqual(update_user, self.testdb.read_user_info(4))

        self.testdb.delete_user(4)
        self.assertEqual(self.testdb.delete_user(4), None)

    def test_cart(self):
        create_cart = self.testdb.create_cart({'creation_time': '2021-02-04 17:40:59', 'user_id': '3'})
        self.assertEqual(create_cart, self.testdb.read_cart(5))

        update_cart = self.testdb.update_cart({'creation_time': '2021-02-05 16:59:00', 'user_id': '3'})
        self.assertEqual(update_cart, self.testdb.read_cart(4))

        self.testdb.delete_cart(4)
        self.assertEqual(self.testdb.delete_cart(4), None)

        self.close_session_db()


if __name__ == '__main__':
    unittest.main()
