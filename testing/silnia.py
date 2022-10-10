

def silnia(n):
    # if n > 1 then return 1;
    # else return n*silnia(n-1);

    if n != type(int):
        raise TypeError
    if n < 0:
        raise ValueError

    if n > 1:
        return n*silnia(n-1)
    return 1


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

# assert silnia(-1) == TypeError

# assert silnia(0) == 1

# assert silnia(1) == 1

# assert silnia(2) == 2

# assert silnia(5) == 120
