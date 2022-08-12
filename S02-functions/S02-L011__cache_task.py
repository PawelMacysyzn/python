import time
import functools


def fib(n):

    if n <= 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)

    return result


@functools.lru_cache(maxsize=100)
def fib_with_cache(n):

    if n <= 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)

    return result


def time_measurement_func(func, n):

    start = time.time()

    for i in range(1, n + 1):
        print('{}! = {}'.format(i, func(i)))

    stop = time.time()
    print('Execution time', stop-start)


# time_measurement_func(fib, 36)
'''
1! = 1
...
36! = 24157817
Execution time 5.104417085647583
'''

time_measurement_func(fib_with_cache, 36)
# CacheInfo(hits=0, misses=36, maxsize=100, currsize=36)
print(fib_with_cache.cache_info())
'''
1! = 1
...
36! = 24157817
Execution time 5.140268325805664
'''
time_measurement_func(fib_with_cache, 36)
# CacheInfo(hits=36, misses=36, maxsize=100, currsize=36)
print(fib_with_cache.cache_info())
'''
1! = 1
...
36! = 24157817
Execution time 0.0030002593994140625
'''
