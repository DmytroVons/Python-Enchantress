import unittest
from unittest import mock
from lectures.tests import resp_util


class TestRequests(unittest.TestCase):

    @mock.patch("lectures.tests.resp_util.make_request", return_value=True)
    def test_parse_response_ok(self, request):
        parsed_resp = resp_util.parse_response()
        self.assertEqual(parsed_resp, "Successful request")
        # self.assertEqual(request.call_count, 1)


if __name__ == "__main__":
    unittest.main()
