import time
import datetime as dt
import sys
import math


class Combinations:

    def __init__(self, products, promotions, customers) -> None:
        self.products = products
        self.promotions = promotions
        self.customers = customers

        self.current_product, self.current_promotion, self.current_customer = 0, 0, 0

    def __next__(self):

        if self.current_customer >= len(self.customers):
            self.current_customer = 0
            self.current_promotion += 1

        if self.current_promotion >= len(self.promotions):
            self.current_promotion = 0
            self.current_product += 1

        if self.current_product >= len(self.products):
            self.current_product = 0
            raise StopIteration()

        item_to_return = self.products[self.current_product], self.promotions[
            self.current_promotion], self.customers[self.current_customer]

        self.current_customer += 1

        return item_to_return

    def __iter__(self):
        return self


def get_sizeof(obj) -> None:
    return print('>>> size of dates is {}'.format(convert_size(sys.getsizeof(obj))))


def convert_size(size_bytes: int) -> str:
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def old_program(products: list, promotions: list, customers: list, time_sleep: int = 10) -> list:

    combinations = []

    for i in products:
        for j in promotions:
            for k in customers:
                combinations.append("{} - {} - {}".format(i, j, k))

    for c in combinations:
        # here an analysis will be done - currently, just nothing happens :)
        pass

    time.sleep(time_sleep)

    return combinations


def new_program(products: list, promotions: list, customers: list, time_sleep: int = 10) -> Combinations:

    combinations = Combinations(products, promotions, customers)

    for c in combinations: pass

    time.sleep(time_sleep)

    return combinations


products = ["Product {}".format(i) for i in range(1, 500)]
print(products)

promotions = ["Promotion {}".format(i) for i in range(1, 50)]
print(promotions)

customers = ['Customer {}'.format(i) for i in range(1, 500)]
print(customers)


time_sleep = 0

start = dt.datetime.now()
get_sizeof(old_program(products, promotions, customers, time_sleep))
stop = dt.datetime.now()
print('Total time: {} for time_sleep: {} '.format(stop - start, time_sleep))

'''
>>> size of dates is 95.59 MB
Total time: 0:00:03.702220 for time_sleep: 0 
'''

print('*'*55)

start = dt.datetime.now()
get_sizeof(new_program(products, promotions, customers, time_sleep))
stop = dt.datetime.now()
print('Total time: {} for time_sleep: {} '.format(stop - start, time_sleep))


'''
>>> size of dates is 48.0 B
Total time: 0:00:04.807127 for time_sleep: 0
'''





