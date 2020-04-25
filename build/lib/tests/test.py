import unittest

from example_package.my_module import my_function


class TestExample(unittest.TestCase):
    def test_example(self):
        actual_output = my_function()
        expected_output = "this is a library function!"
        self.assertEqual(actual_output, expected_output)
