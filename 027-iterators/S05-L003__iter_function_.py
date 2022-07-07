aTuple = (1, 2, 3, 4, 5)


# for x in aTuple:
#     print(x)
# '''
# 1
# 2
# 3
# 4
# 5
# '''

# print(next(aTuple))
# '''
# Traceback (most recent call last):
#   File "c:\Users\macyszyp\Documents\DriveWare\Composer\python\027-iterators\S05-L003__iter_function_.py", line 14, in <module>
#     print(next(aTuple))
# TypeError: 'tuple' object is not an iterator
# '''

# it = iter(aTuple)

# print(next(it)) #   1
# print(next(it)) #   2


aList = [1, 2, 3, 4, 5]

# for x in aList:
#     print(x)
# '''
# 1
# 2
# 3
# 4
# 5
# '''

# print(next(aList))
# '''
# Traceback (most recent call last):
#   File "c:\Users\macyszyp\Documents\DriveWare\Composer\python\027-iterators\S05-L003__iter_function_.py", line 40, in <module>
#     print(next(aList))
# TypeError: 'list' object is not an iterator
# '''

# it = iter(aList)

# print(next(it)) #   1
# print(next(it)) #   2


aSet = {1, 2, (3,4), 'another element', 3, 4}

# for x in aSet:
#     print(x)
# '''
# 1
# 2
# 3
# 4
# (3, 4)
# another element
# '''

# print(next(aSet))
# '''
# Traceback (most recent call last):
#   File "c:\Users\macyszyp\Documents\DriveWare\Composer\python\027-iterators\S05-L003__iter_function_.py", line 67, in <module>
#     print(next(aSet))
# TypeError: 'set' object is not an iterator
# '''

# it = iter(aSet)

# print(next(it)) #   1
# print(next(it)) #   2


with open(r'C:\TEMP\lines.txt', 'r') as file:
    for line in file:
        print(line)

# '''
# line 1

# line 2

# line 3

# the last line
# '''

# with open('C:\TEMP\lines.txt', 'r') as file:
#     while True:
#         print(next(file))

# """
# line 1

# line 2

# line 3

# the last line

# Traceback (most recent call last):
#   File "c:\Users\macyszyp\Documents\DriveWare\Composer\python\027-iterators\S05-L003__iter_function_.py", line 97, in <module>
#     print(next(file))
# StopIteration
# """

with open('C:\TEMP\lines.txt', 'r') as file:
    while True:
      try:
        print(next(file))
      except StopIteration:
        break

'''
line 1

line 2

line 3

the last line
'''

with open('C:\TEMP\lines.txt', 'r') as file:
  print(file.__next__()) #  line 1
  print(file.__next__()) #  line 2


