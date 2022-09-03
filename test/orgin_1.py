'''
Prepare the functions to check if the person of the given age is of legal age

EN/PL

Przygotuj funkcje sprawdzającą czy osoba o przekazanym wieku jest osoba pełnoletnią 

'''


def is_adult(age: int) -> bool:
    return age >= 18


def test_is_adult():
    # given
    age = 18

    # when
    result = is_adult(age)

    # then
    assert result == True
    assert is_adult(20)


def test_is_not_adult():
    assert not is_adult(17)
    assert not is_adult(3)



'''
put the command in cmd:
py -m pytest .\orgin_1.py
'''