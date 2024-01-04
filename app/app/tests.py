"""
sample test file
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """
    sample test class
    """

    def test_add_numbers(self):
        """
        test adding numbers
        """
        res = calc.add(3, 8)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """
        test subtracting numbers
        """
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
