def double(x):
    return x*2


x = 10
x = double(x)
print(x)  # 20


x = 10
f = lambda x: x*2
print(f(x))  # 20
print(f)  # <function <lambda> at 0x0000020F3858AEF0>


def power(x, y):
    return x**y


x, y = 5, 3
print(power(x, y))  # 125

f = lambda x,y: x**y
print(f(x, y))  # 125   



list_numbers = [1, 2, 3, 4, 11, 14, 15, 20, 21]


def is_odd(x):
    return x % 2 != 0


print(is_odd(7), is_odd(4)) # True False

filter_list = filter(is_odd, list_numbers)
print(filter_list) # <filter object at 0x000002050D43BE50>
print(list(filter_list)) # [1, 3, 11, 15, 21]


filter_list = list(filter(lambda x: x % 2 != 0, list_numbers))
print(filter_list)  # [1, 3, 11, 15, 21]

print(list(filter(lambda x: x%2 != 0, list_numbers)))    # [1, 3, 11, 15, 21]


def generate_multyply_function(n):
    return lambda x: n*x 

mul_2 = generate_multyply_function(2)
mul_3 = generate_multyply_function(3)


print(mul_2(13), mul_3(8)) # 26 24