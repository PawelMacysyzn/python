import itertools as it
import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

for e, tiune in enumerate(it.combinations(notes, 4)):
    # print(e+1, tiune)
    pass


print("4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities".format(
    math.factorial(len(notes))/math.factorial(len(notes) - 4)))
# 4-notes melody, notes cannot repeat - it is variation without repeating - there are 840.0 possibilities


input('Press enter')
 
# for e, x in enumerate(it.product(notes, repeat=4)):
#     print(e+1, x)
 
print("4-notes melody - notes can repeat - it is variation with repeating - there are {} possibilities".format(
        pow(len(notes), 4)))
# 4-notes melody - notes can repeat - it is variation with repeating - there are 2401 possibilities



















