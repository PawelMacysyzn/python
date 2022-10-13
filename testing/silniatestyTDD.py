# python -m unittest -v silnia_test.py
import unittest
from silniaTDD import silnia, SilniaTypeError


class TestSilniaTDD(unittest.TestCase):

    def test_silnia_zero(self):
        self.assertEqual(silnia(0), 1)

    def test_silnia_one(self):
        self.assertEqual(silnia(1), 1)

    def test_silnia_two(self):
        self.assertEqual(silnia(2), 2)

    def test_silnia_five(self):
        self.assertEqual(silnia(5), 120)

    def test_silnia_minus_one(self):
        self.assertRaises(ValueError, silnia, -1)

    def test_silnia_minus_two(self):
        self.assertRaises(ValueError, silnia, -2)

    def test_silnia_str(self):
        self.assertRaises(SilniaTypeError, silnia, 'sassa')