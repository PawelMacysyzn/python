import random


def random_with_sum(number_of_values, asserted_sum):

    # counter of attempts to draw values before you manage to draw numbers that add up to asserted_sum (we have 100)
    trial = 0
    # counting board
    numbers = list(range(number_of_values))

    while True:

        trial += 1
        for i in range(number_of_values):
            numbers[i] = random.randint(1,100)

        if sum(numbers) == asserted_sum:
            yield (trial, numbers)
            trial = 0


number_of_values = 3
asserted_sum = 100


for i in range(10):
    x, y = random_with_sum(number_of_values, asserted_sum).__next__()
    print('{:3d} - {}'.format(x, y))

'''
77 [18, 52, 30]
222 [38, 47, 15]
682 [1, 94, 5]
63 [77, 20, 3]
174 [29, 65, 6]
399 [67, 17, 16]
43 [27, 56, 17]
77 [58, 18, 24]
45 [58, 32, 10]
99 [48, 36, 16]
'''