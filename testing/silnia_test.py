# python -m unittest -v silnia_test.py
import unittest
from silnia import silnia
import sys

# --------------------------------------------------------------------------------
# path_fun = r'C:\Users\pmacyszyn_adm\Documents\python\python\Szkolenie_embedded'
# sys.path.append(path_fun)
# import calculator

# calc = calculator.Calcute()
# print(calc.add(2,2))
# --------------------------------------------------------------------------------


class TestSilnia(unittest.TestCase):

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

    def test_silnia_str(self):
        self.assertRaises(TypeError, silnia, 'sassa')





# Klasy rownowaznosci:
"""
# Klassa rownowaznosci (abstrakcji lub podzbiorrownowaznosci) #
!(-∞) => error
dla n < 0

wartosc brzekowa (-1)

e.g.
!(-1) => error

# Klassa rownowaznosci (abstrakcji) #
dla n >= 0 and n < 2
!0 => 1
!1 => 1

wartosc brzekowa (0, 1)


# Klassa rownowaznosci (abstrakcji) #
dla n > 1

wartosc brzekowa (2)

e.g.
!2 => 2 
"""



# Test case:

# assert silnia(-1) == ValueError

# assert silnia(0) == 1

# assert silnia(1) == 1

# assert silnia(2) == 2

# assert silnia(5) == 120

# assert silnia('sasassa') == TypeError
















































