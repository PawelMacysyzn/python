
def silnia(n):
    # if n > 1 then return 1;
    # else return n*silnia(n-1);

    if type(n) != int:
        raise TypeError
    if n < 0:
        raise ValueError

    if n > 1:
        return n*silnia(n-1)
    return 1

def main():
    pass


if __name__ == '__main__':
    main()