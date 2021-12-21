from unittest import TestCase
from unittest.mock import patch

import api

class TestApi(TestCase):

    def test_xpto(self):
        self.assertEqual('foo'.upper(), 'FOO')


    @patch("api.get_hit_count", return_value="10")
    def test_hello(self, hit_count):
        expected_return = "Hello World! I have been seen {} times.\n".format(hit_count.return_value)

        actual = api.hello()
        self.assertEqual(actual, expected_return)
