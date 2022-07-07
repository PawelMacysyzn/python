import datetime as dt
import sys, math


def convert_size(size_bytes: int) -> str:
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


start = dt.datetime.now()
print('Execution started at: {}'.format(start))


# dates = [dt.date(2000, 1, 1) + dt.timedelta(days=i) for i in range(2500000)]
# print('size of dates is {}'.format(convert_size(sys.getsizeof(dates))))

# for _ in range(1):
#     for d in dates: pass

class MilionDays:

    def __init__(self, year, month, day, maxdays) -> None:

        self.date = dt.date(year, month, day)
        self.maxdays = maxdays

    def __next__(self) -> dt.date:

        if self.maxdays <= 0: raise StopIteration()
        ret = self.date
        self.date += dt.timedelta(days=1)
        self.maxdays -= 1
        return ret

    def __iter__(self):
        return self

    def get_sizeof(self) -> None:
        return print('>>> size of dates is {}'.format(convert_size(sys.getsizeof(self))))


md = MilionDays(2000, 1, 1, 2500000)
md.get_sizeof()

for d in md:
    pass


stop = dt.datetime.now()
print('Execution started at: {}'.format(stop))
print('Total time: {}'.format(stop - start))
