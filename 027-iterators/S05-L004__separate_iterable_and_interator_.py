import datetime as dt


class MilionDaysIterator:
    def __init__(self, date, maxdays) -> None:
        self.date = date
        self.maxdays = maxdays

    def __next__(self) -> dt.date:
        if self.maxdays <= 0:
            raise StopIteration()
        ret = self.date
        self.maxdays -= 1
        self.date += dt.timedelta(days=1)
        return ret

    # def __iter__(self):
    #     return self


class MilionDays:

    def __init__(self, year, month, day, maxdays) -> None:

        self.date = dt.date(year, month, day)
        self.maxdays = maxdays
        self.iterator = MilionDaysIterator(self.date, self.maxdays)

    def __iter__(self):
        return self.iterator


md = MilionDays(2000, 1, 1, 3)

# next(md)
print(next(iter(md))) # 2000-01-01
print(next(iter(md))) # 2000-01-02     

for d in md:
    pass

