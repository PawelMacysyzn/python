import datetime as dt
import math


def MilionDays(year, month, day, maxdays):

    date = dt.date(year, month, day)

    for i in range(maxdays):
        yield (date + dt.timedelta(days=i))


for d in MilionDays(2000, 1, 1, 3):
    print(d)

'''
2000-01-01
2000-01-02
2000-01-03
'''

def GetMagicNumbers():
    yield (22)
    yield (4)
    yield (5)


r = GetMagicNumbers()

# print(next(r))
# print(r.__next__())
# print(next(r))

# '''
# 22
# 4
# 5
# '''

for m in r:
    print(m)

'''
22
4
5
'''









