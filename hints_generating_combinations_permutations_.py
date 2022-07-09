# ------------------------------------------
### Examples ###

import itertools as it

mylist = ['a', 'b', 'c', 'd']

for e, x in enumerate(it.product(mylist, repeat=3)):
    pass
print(e+1) # 64

for e, x in enumerate(it.combinations(mylist, 3)):
    pass
print(e+1) # 4

for e, x in enumerate(it.combinations_with_replacement(mylist, 3)):
    pass
print(e+1) # 20

for e, x in enumerate(it.permutations(mylist, 3)):
    pass
print(e+1) # 24


# ------------------------------------------
# Permutacions #

import itertools as it

mylist = ['a', 'b', 'c']

for permutations in it.permutations(mylist, 3):
    print(permutations)

'''
('a', 'b', 'c')
('a', 'c', 'b')
('b', 'a', 'c')
('b', 'c', 'a')
('c', 'a', 'b')
('c', 'b', 'a')
'''
# ------------------------------------------


# ------------------------------------------
# Combinations #

import itertools as it

mylist = ['a', 'b', 'c', 'd']

for combinations in it.combinations(mylist, 3):
    print(combinations)

'''
('a', 'b', 'c')
('a', 'b', 'd')
('a', 'c', 'd')
('b', 'c', 'd')
'''
# ------------------------------------------


# ------------------------------------------
# Combinations with replacement #

import itertools as it

mylist = ['a', 'b', 'c']

for combinations in it.combinations_with_replacement(mylist, 3):
    print(combinations)

'''
('a', 'a', 'a')
('a', 'a', 'b')
('a', 'a', 'c')
('a', 'b', 'b')
('a', 'b', 'c')
('a', 'c', 'c')
('b', 'b', 'b')
('b', 'b', 'c')
('b', 'c', 'c')
('c', 'c', 'c')
'''
# ------------------------------------------


# ------------------------------------------
# All possible combinations with repetitions #

import itertools as it

mylist = ['a', 'b', 'c']

for x in it.product(mylist, repeat=3):
    print(x)

'''
('a', 'a', 'a')
('a', 'a', 'b')
('a', 'a', 'c')
     ...
('c', 'b', 'c')
('c', 'c', 'a')
('c', 'c', 'b')
('c', 'c', 'c')
'''
# ------------------------------------------