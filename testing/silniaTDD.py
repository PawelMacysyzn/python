class SilniaTypeError(Exception):
    pass


def silnia(n):

    if type(n) != int:
        raise SilniaTypeError

    if n < 0:
        raise ValueError
    

    if n == 0 or n == 1: 
        return 1
    else:
        acc = 1        
        for i in range(2, n + 1):
            acc = acc * i
        return acc
                   
# print(silnia('sassa'))