
# ------------------------------------------
mesage = "Enter int: "
# The walrus operator
print(x:=int(input(mesage)) + 6)
# ------------------------------------------


# ------------------------------------------
known_types = 'cake:muffin:meringue:biscuit:eclair:christmas:pretzel:other' # type<str>

# Nazwał bym to wyłuskiwaniem xd   *

print(*known_types)
'''
c a k e : m u f f i n : m e r i n g u e : b i s c u i t : e c l a i r : c h r i s t m a s : p r e t z e l : o t h e r
'''
print(known_types.split(':')) # type<list>
'''
['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
'''
print(*known_types.split(':')) # type<none>
'''
cake muffin meringue biscuit eclair christmas pretzel other

'''
# ------------------------------------------


# ------------------------------------------
import glob


f = glob.glob('c:/temp/*.txt')   # catalog/*.format_file

print(f)
# retururn list of .txt files 
# ------------------------------------------


# ------------------------------------------
# Infinite generator #

def generator():
    while True:
        try:
            yield 1
            yield 2
            yield 3
        except StopIteration:
            break

d = generator()
print(d.__next__()) #   1
print(d.__next__()) #   2
print(d.__next__()) #   3
print(d.__next__()) #   1
# ------------------------------------------


# ------------------------------------------
# Return a number between 3 and 9 (both included):
import random

print(random.randint(3, 9))
# ------------------------------------------


# ------------------------------------------
# new convenience notation for big numbers introduced #
# With Python 3.6 (and PEP-515)

number_with_ = 1_000_000
print(number_with_) # 1000000

# Stanowczo poprawia to czytelność kodu :), warto to stosować !

# ------------------------------------------


# ------------------------------------------
# Using the dir() function to list methods in a class

print(dir(str)) # show all methods in class str

# ------------------------------------------


# ------------------------------------------
# The count() method returns the number of times the specified element appears in the list
# For class List #

numbers = [2, 3, 5, 2, 11, 2, 7]

# check the number of occurrences of "2"
count = numbers.count(2)

print('Count of 2:', count)

# Output: Count of 2: 3

# ------------------------------------------











 