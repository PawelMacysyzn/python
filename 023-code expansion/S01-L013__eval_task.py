import math

def inf_obj(object):
    print(type(object), end='')
    print('len:',len(object))
    print('{}'.format(object))
    print('-'*25*2)

'''
import numpy as np
list_of_argument_as_numpy = list(np.arange(0, 1, 0.1))
inf_obj(list_of_argument_as_numpy)
'''
# <class 'list'>len: 10
# [0.0, 0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6000000000000001, 0.7000000000000001, 0.8, 0.9]
'''
list_of_argument_normal_divide = [x * 0.1 for x in range(0, 10)]
inf_obj(list_of_argument_normal_divide)
'''
# <class 'list'>len: 10
# [0.0, 0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6000000000000001, 0.7000000000000001, 0.8, 0.9]
'''
list_of_argument_normal_divide = [x/10 for x in range(0, 10)]
inf_obj(list_of_argument_normal_divide)
'''
# <class 'list'>len: 10
# [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
'''
list_of_argument_as_np_linspace = list(np.linspace(0,1,10,endpoint=False))
inf_obj(list_of_argument_as_np_linspace)
'''
# <class 'list'>len: 10
# [0.0, 0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6000000000000001, 0.7000000000000001, 0.8, 0.9]



list_of_arguments = [x/10 for x in range(0, 100)]
# inf_obj(list_of_arguments)


while True:
    formula = input("Please enter a formula, use 'x' as the argument: ")
    if formula.lower().find('x') != -1 : 
        break
    else:
        print('You did not enter "x"')
        
for x in list_of_arguments:
    print('{} = {:.2f}'.format(x, eval(formula)))
