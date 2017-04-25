import unittest

from my_function import my_prime_numbers

class prime_number_test(unittest.TestCase):

    def test_first_prime_number(self):

        self.assertEqual(my_prime_numbers(2)[1], [2], msg="the results are invalid")

    def test_second_prime_number(self):

        self.assertEqual(my_prime_numbers(3)[1], [2,3], msg="the results are invalid")

    def test_third_prime_number(self):
        self.assertEqual(my_prime_numbers(1)[1], [], msg="the results are invalid")

    def test_arg_is_int(self):
        self.assertIsInstance(my_prime_numbers(1)[0], int, msg="the argument is not integer")

    def test_prime_number_in_list(self):
        self.assertIsInstance(my_prime_numbers(1)[1], list, msg="the results are not in a list")