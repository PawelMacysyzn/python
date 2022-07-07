import datetime as dt

class Millionsdays:

    def __init__(self, year, month, day, maxdays) -> None:
        self.date = dt.datetime(year, month, day)
        self.maxdays = maxdays

    def __getitem__(self, item):
        if item <= self.maxdays:
            return self.date + dt.timedelta(days=item)
        else:
            raise StopIteration()


# md = Millionsdays(2000,1,1,2500000)

# print(md[0], md[1], md[2], md[100000])
'''
2000-01-01 00:00:00 2000-01-02 00:00:00 2000-01-03 00:00:00 8844-10-07 00:00:00
'''

md = Millionsdays(2000,1,1,20)

it = iter(md)


print(next(it))
print(next(it))
print(next(it))


for d in md:
    print(d)

'''
2000-01-01 00:00:00
        ...
2000-01-21 00:00:00
'''

