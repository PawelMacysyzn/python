def combinations(products, promotions, customers):

    for current_product in products:
        for current_promotion in promotions:
            for current_customer in customers:
                yield("{} - {} - {}".format(current_product, current_promotion, current_customer))


products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]

for i, c in enumerate(combinations(products, promotions, customers)):
    print('[{:2d}] - {}'.format(i, c))
