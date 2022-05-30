workDays = [19, 21, 22, 21, 20, 22]
months = ['I', 'II', 'III', 'IV', 'V', 'VI']

enumerate_workDays = dict(enumerate(workDays))

print(enumerate_workDays)                   # {0: 19, 1: 21, 2: 22, 3: 21, 4: 20, 5: 22}

zip_workDays = dict(zip(months ,workDays))  # {'I': 19, 'II': 21, 'III': 22, 'IV': 21, 'V': 20, 'VI': 22}
print(zip_workDays)


for key in zip_workDays:
    print('Key is',key, 'value is', zip_workDays[key])
'''
Key is I value is 19
Key is II value is 21
Key is III value is 22
Key is IV value is 21
Key is V value is 20
Key is VI value is 22
'''

for value in zip_workDays.values():
    print('the value is', value)
'''
the value is 19
the value is 21
the value is 22
the value is 21
the value is 20
the value is 22
'''