listA = list(range(6))
listB = list(range(6))


gen = ((a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)
# <class 'generator'>
print(type(gen))
# <generator object <genexpr> at 0x000002C3C54F9930>
print(gen)

# (1, 0)
print(next(gen))
# (1, 2)
print(next(gen))
# ******************************
print('*'*30)
for x in gen:
    print(x)
'''
(1, 4)
(3, 0)
(3, 2)
(3, 4)
(5, 0)
(5, 2)
(5, 4)
'''
# Traceback (most recent call last): 
# StopIteration
# print(next(gen))


# ******************************
print('*'*30)


gen = ((a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)

while True:
    try:
        print(next(gen))
    except StopIteration:
        print('all values have been generated')
        break
'''
(1, 0)
(1, 2)
(1, 4)
(3, 0)
(3, 2)
(3, 4)
(5, 0)
(5, 2)
(5, 4)
'''