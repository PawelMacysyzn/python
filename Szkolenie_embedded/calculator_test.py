import unittest
from calculator import *


class TestCalcute(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calcute()

    def test_addition_of_two_small_numbers(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)

    def test_addition_of_two_big_numbers(self):
        result = self.calc.add(2_000_000, 4_000_000)
        self.assertEqual(6_000_000, result)


if __name__ == "__main__":
    unittest.main()