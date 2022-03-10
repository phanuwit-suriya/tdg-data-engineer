import unittest

from section1 import is_palindrome
from section2 import reverse_string


class TestIsPalindrome(unittest.TestCase):
    def test_one_digit_input(self):
        for i in range(1, 10):
            with self.subTest(i=i):
                self.assertEqual(is_palindrome(i), True)

    def test_even_length_palindrome_input(self):
        n = 12345678900987654321
        self.assertEqual(is_palindrome(n), True)

    def test_event_length_not_palindrome_input(self):
        n = 12345678901234567890
        self.assertEqual(is_palindrome(n), False)

    def test_odd_length_palindrome_input(self):
        n = 1234567890987654321
        self.assertEqual(is_palindrome(n), True)

    def test_odd_length_not_palindrome_input(self):
        n = 1234567890123456789
        self.assertEqual(is_palindrome(n), False)


class TestReverseString(unittest.TestCase):
    def test_empty_array_input(self):
        inp = []
        out = []
        self.assertEqual(reverse_string(inp), out)

    def test_one_element_in_array_input(self):
        inp = ["a"]
        out = ["a"]
        self.assertEqual(reverse_string(inp), out)

    def test_odd_number_of_element_in_array_input(self):
        inp = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        out = ["i", "h", "g", "f", "e", "d", "c", "b", "a"]
        self.assertEqual(reverse_string(inp), out)

    def test_even_number_of_element_in_array_input(self):
        inp = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q"]
        out = ["q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.assertEqual(reverse_string(inp), out)


if __name__ == "__main__":
    unittest.main(verbosity=1)
