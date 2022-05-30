workDays = [19, 21, 22, 21, 20, 22]


enumerate_workDays = list(enumerate(workDays))

print(workDays)                 # [19, 21, 22, 21, 20, 22]
print(enumerate_workDays)       # [(0, 19), (1, 21), (2, 22), (3, 21), (4, 20), (5, 22)]

for pos, value in enumerate_workDays:
    print('{}. {}'.format(pos, value))
'''
0. 19
1. 21
2. 22
3. 21
4. 20
5. 22
'''
    
months = ['I', 'II', 'III', 'IV', 'V', 'VI']

monthsDays = list(zip(months, workDays)) 
print(monthsDays)                 # [('I', 19), ('II', 21), ('III', 22), ('IV', 21), ('V', 20), ('VI', 22)]



for pos, (m, d) in enumerate(zip(months, workDays)):
    print('Position {} month {} days {}'.format(pos, m, d))
'''
Position 0 month I days 19
Position 1 month II days 21
Position 2 month III days 22
Position 3 month IV days 21
Position 4 month V days 20
Position 5 month VI days 22
'''
