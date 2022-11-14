import time
import functools

iterations = 18


def wrapper_time(a_function):
    def a_wrapped_function(*args, **kwargs):

        time_start = time.time()
        v = a_function(*args, **kwargs)
        time_stop = time.time()
        print("Duration: {} sec".format(time_stop-time_start))
        return v

    return a_wrapped_function


def wrapper_delay(a_function):
    def a_wrapped_function(*args, **kwargs):
      
        time.sleep(5)
        return a_function(*args, **kwargs)
    return a_wrapped_function


            
def get_sequence(n):

    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v


@wrapper_delay
@wrapper_time
def wrapped_get_sequence(x):
    return get_sequence(x)


print(wrapped_get_sequence(iterations))
