import random


# Zaimplementować funkcję losowego tasowania bez użycia modułu random i funkcji randint().
# Jednym ze sposobów na to jest wykorzystanie funkcji hashującej.

# Oto przykładowa implementacja losowego tasowania z wykorzystaniem funkcji hashującej:

mylist = list(range(1, 66))


def random_shuffle(lst):
    n = len(lst)
    for i in range(n-1, 0, -1):
        j = hash(str(i)) % (i+1)
        lst[i], lst[j] = lst[j], lst[i]
    return lst

print(mylist)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]

print(random_shuffle(mylist))
# [20, 12, 4, 57, 7, 41, 23, 19, 53, 10, 51, 1, 30, 27, 45, 52, 5, 38, 47, 55, 50, 64, 34, 24, 6, 33, 43, 18, 46, 48, 2, 11, 61, 58, 49, 8, 40, 59, 13, 25, 44, 60, 35, 9, 32, 15, 56, 31, 21, 62, 14, 39, 17, 22, 36, 42, 3, 65, 28, 37, 26, 63, 29, 54, 16]

print(random.shuffle(mylist))
# [12, 60, 46, 20, 34, 3, 22, 16, 62, 48, 30, 17, 1, 7, 64, 13, 5, 40, 39, 21, 25, 58, 32, 37, 15, 49, 35, 19, 31, 8, 54, 6, 36, 41, 14, 10, 63, 29, 4, 61, 44, 47, 43, 55, 53, 56, 65, 18, 52, 28, 27, 2, 38, 59, 42, 24, 51, 23, 33, 57, 45, 9, 26, 50, 11]