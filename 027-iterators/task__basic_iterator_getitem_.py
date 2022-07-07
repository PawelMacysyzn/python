class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

    def __getitem__(self, item):

        if item > (len(self.products) * len(self.promotions) * len(self.customers)):
            raise StopIteration()
        else:
            pos_products = item // (len(self.promotions) * len(self.customers))

            item = item % (len(self.promotions) * len(self.customers))

            pos_promotions = item // len(self.customers)

            item = item % len(self.customers)

            pos_customers = item

            return "{} - {} - {}".format(self.products[pos_products], self.promotions[pos_promotions], self.customers[pos_customers])



products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]

combinations = Combinations(products, promotions, customers)



# for i in range((len(products) * len(promotions) * len(customers))):
#     print('{} - {}'.format(i, combinations[i]))

# '''
# 0 - Product 1 - Promotion 1 - Customer 1
#                     ...
# 29 - Product 3 - Promotion 2 - Customer 5
# '''

combinations_iter = iter(combinations)

for c in combinations_iter:
    print(c)

'''
0 - Product 1 - Promotion 1 - Customer 1
                    ...
29 - Product 3 - Promotion 2 - Customer 5
'''

# print(next(combinations_iter))

# '''
# Traceback (most recent call last):
#   File "c:\Users\macyszyp\Documents\DriveWare\Composer\python\027-iterators\task__basic_iterator_getitem_.py", line 54, in <module>
#     print(next(combinations_iter))
# StopIteration
# '''