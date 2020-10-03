from rearranging_names import rearranging_names
import unittest

class TestRearrange(unittest.TestCase):
    def test_names(self):
        testcase = "Kapadia, Shreya"
        expected = "Shreya Kapadia"

        self.assertEqual(rearranging_names(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""

        self.assertEqual(rearranging_names(testcase), expected)

    def test_double_name(self):
        testcase = "Kapadia, Shreya D."
        expected = "Shreya D. Kapadia"

        self.assertEqual(rearranging_names(testcase), expected)

    def test_single_name(self):
        testcase = "Shreya"
        expected = "Shreya"

        self.assertEqual(rearranging_names(testcase), expected)

unittest.main()
