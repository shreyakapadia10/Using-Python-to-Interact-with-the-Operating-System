from raise_assert import validate_username
import unittest

class TestValidateUsername(unittest.TestCase):
    """ To test various test cases for valid username """

    def test_valid(self):
        self.assertEqual(validate_username("validuser", 3), True)

    def test_too_short(self):
        self.assertEqual(validate_username("abc", 5), False)

    def test_invalid_chars(self):
        self.assertEqual(validate_username("invalid_username", 5), False)

    def test_invalid_minlen(self):
        # assertRaises to test for the errors we raised using raise
        #1st Parameter - Type of Error, 2nd Parameter - function we want to taste, 3rd and 4th Parameter - any arguments the function takes
        self.assertRaises(ValueError, validate_username, "user", -1)

unittest.main()
