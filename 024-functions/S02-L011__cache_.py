import time
import functools

# *************************************
# !!! FOR DETERMINING FUNCTIONS ONLY !!!
# *************************************
@functools.lru_cache()  

# *************************************
def Factorial(n):

    time.sleep(0.1)

    if n == 1:
        return 1
    else:
        return n * Factorial(n-1)


print(Factorial.cache_info()) # CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)


start = time.time()
for i in range(1, 11):
    print('{}! = {}'.format(i, Factorial(i)))
stop = time.time()

print('Execution time', stop-start)


# before, without @functools.lru_cache()  
'''
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
10! = 3628800
Execution time 5.510935306549072
'''

# after
'''
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
10! = 3628800
Execution time 1.003988265991211
'''

print(Factorial.cache_info()) # CacheInfo(hits=9, misses=10, maxsize=128, currsize=10)

start = time.time()
for i in range(1, 11):
    print('{}! = {}'.format(i, Factorial(i)))
stop = time.time()

print('Execution time', stop-start)

'''
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
10! = 3628800
Execution time 0.0009999275207519531
'''