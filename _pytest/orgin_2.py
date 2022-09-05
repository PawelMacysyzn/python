'''
Prepare a function that will print the area of a triangle based on the height and length of the base

EN/PL

Przygotuj funkcję, która na podstawie wysokości oraz długości podstawy wyswietli (print) pole trujkąta 

'''

def get_triangle_field(base: int, height: int) -> float:
    print(0.5 * base * height, end='')


def test_triangle_area(capsys):
    # try
    base = 10
    height = 8

    # when
    get_triangle_field(base, height)
    out, err = capsys.readouterr()

    # then
    assert out == '40.0'
    

































