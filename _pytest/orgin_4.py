'''
Function sorting the list of first names:
- in alphabetical order of the first letter,
- in alphabetical order of the last letter,
- according to the length of the name

EN/PL

Funkcja sortująca listę imion:
- w kolejnosci alfabetycznej pierwszej litery,
- w kolejnosci alfabetycznej ostatniej litery,
- według długosci imienia  
'''

import pytest


def sort_by(names: str, first_letter: bool = False, last_letter: bool = False, lenght: bool = False):
    if first_letter:
        names.sort()

    if last_letter:
        names.sort(key=lambda name: name[::-1])

    if lenght:
        # names.sort(key = lambda x: len(x))
        # equal
        names.sort(key = len)
    return names


class TestSort:

    @pytest.fixture
    def names(self):
        return ['Alina', 'Ewa', 'Paulina', 'Maciej']

    def test_sort(self, names):
        # when
        sorted_name = sort_by(names, first_letter=True)

        # then
        assert sorted_name == ['Alina', 'Ewa', 'Maciej', 'Paulina']

    def test_reverse_sort(self, names):
        # when
        sorted_name = sort_by(names, last_letter=True)

        # then
        assert sorted_name == ['Alina', 'Paulina', 'Ewa', 'Maciej']

    def test_by_length(self, names):
        #  when
        sorted_name = sort_by(names, lenght=True)

        #then
        assert sorted_name == ['Ewa', 'Alina', 'Maciej', 'Paulina']