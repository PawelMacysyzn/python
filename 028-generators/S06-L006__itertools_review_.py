import itertools
import operator


data = [1, 2, 3, 4, 5]
result = itertools.accumulate(data, operator.mul)
for each in result:
    print(each)

print('-'*66)

'''
1
2  
6  
24 
120
'''

for i in itertools.count(10, 3):
    print(i)
    if i > 20:
        break
'''
10
13
16
19
22
'''
print('-'*66)
'''
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Ocy', 'Nov', 'Dec']
for m in itertools.cycle(months):
    print(m)

# infinite loop cycle #

'''
print('-'*66)

clors_basic = ['red', 'yellow', 'blue']
clors_mix = ['green', 'orange', 'violet']
result = itertools.chain(clors_basic, clors_mix)
for each in result:
    print(each)
'''
red
yellow
blue
green
orange
violet
'''
print('-'*66)

cars = ['Ford', 'Opel', 'Toyota', 'Skoda']
selections = [True, False, True, False]
result = itertools.compress(cars, selections)
for each in result:
    print(each)
'''
Ford
Toyota
'''
print('-'*66)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

result = itertools.dropwhile(lambda x: x<5, data)
for each in result:
    print(each)

'''
5
6
7
8
9
10
1
'''
print('-'*66)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]

result = itertools.filterfalse(lambda x: x<5, data)
for each in result:
    print(each)

'''
5
6
7
8
9
10
'''
print('-'*66)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Ocy', 'Nov', 'Dec']
result = itertools.islice(months, 6, 8)
for each in result:
    print(each)

'''
Jul
Aug
'''
print('-'*66)

spades = ['Hearts', 'Tiles', 'Clovers', 'Pikes']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']
result = itertools.product(spades, figures)
for each in result:
    print(each)

'''
('Hearts', 'Ace')
('Hearts', 'King')
('Hearts', 'Queen')
('Hearts', 'Jack')
('Hearts', '10')
('Hearts', '9')
('Tiles', 'Ace')
('Tiles', 'King')
('Tiles', 'Queen')
('Tiles', 'Jack')
('Tiles', '10')
('Tiles', '9')
('Clovers', 'Ace')
('Clovers', 'King')
('Clovers', 'Queen')
('Clovers', 'Jack')
('Clovers', '10')
('Clovers', '9')
('Pikes', 'Ace')
('Pikes', 'King')
('Pikes', 'Queen')
('Pikes', 'Jack')
('Pikes', '10')
('Pikes', '9')
'''
print('-'*66)


# for i in itertools.repeat('tell me more'):
#     print(i)

# infinite loop cycle #

'''
    ...
tell me more
tell me more
tell me more
tell me more
tell me more
tell me more
    ...
'''

for i in itertools.repeat('tell me more', 5):
    print(i)
'''
tell me more
tell me more
tell me more
tell me more
tell me more
'''


print('-'*66)

data = [(1, 2), (3, 4), (5, 6)]
result = itertools.starmap(operator.add, data)
for each in result:
    print(each)

'''
3
7
11
'''
print('-'*66)


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = itertools.takewhile(lambda x: x<5, data)
for each in result:
    print(each)
'''
1
2
3
4
'''
print('-'*66)


cars = ['Ford', 'Opel', 'Toyota', 'Skoda']
cars1, cars2 = itertools.tee(cars)

for each in cars1:
    print(each)
print('-'*6)
for each in cars2:
    print(each)

'''
Ford
Opel
Toyota
Skoda
------
Ford
Opel
Toyota
Skoda
'''
print('-'*66)


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Ocy', 'Nov', 'Dec']
plan = ['busy', 'busy', 'busy', 'busy', 'busy', 'busy', 'free', 'free']

result = itertools.zip_longest(months, plan, fillvalue= 'unknown')
for each in result:
    print(each)

'''
('Jan', 'busy')
('Feb', 'busy')
('Mar', 'busy')
('Apr', 'busy')
('May', 'busy')
('Jun', 'busy')
('Jul', 'free')
('Aug', 'free')
('Sep', 'unknown')
('Ocy', 'unknown')
('Nov', 'unknown')
('Dec', 'unknown')
'''
print('-'*66)






















