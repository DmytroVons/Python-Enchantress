import unittest
import sys
import falcon


def external_resource_available():
    return True


class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(
        falcon.__version__ < '3.0.0.', "not supported in this library version"
    )
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass


# or from console python3 -m unittest lectures/tests/test_skip.py
if __name__ == '__main__':
    # verbosity attribute configs how detailed output should be
    unittest.main(verbosity=1)
