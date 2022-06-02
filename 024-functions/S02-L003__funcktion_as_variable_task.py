def double(x):
    return 2 *x
 
def square(x):
    return x**2
 
def negative(x):
    return -x
 
def div2(x):
    return x/2


number = 8

transformations =[double, square, div2, negative]


print('Starting transformations')
for transformation in transformations:

    tmp_return_value = number
    tmp_return_value = transformation(tmp_return_value)
    print('{}: temporal result is {} for {}'.format(transformation.__name__, tmp_return_value, number))

'''
Starting transformations
double: temporal result is 16 for 8
square: temporal result is 64 for 8
div2: temporal result is 4.0 for 8
negative: temporal result is -8 for 8
'''



transformations_2 = [square, square, div2, double]

print('Starting transformations_2')
for transformation in transformations_2:

    tmp_return_value = number
    tmp_return_value = transformation(tmp_return_value)
    print('{}: temporal result is {} for {}'.format(transformation.__name__, tmp_return_value, number))

'''
Starting transformations_2
square: temporal result is 64 for 8
square: temporal result is 64 for 8
div2: temporal result is 4.0 for 8
double: temporal result is 16 for 8
'''
