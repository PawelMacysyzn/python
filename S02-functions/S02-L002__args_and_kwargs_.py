from turtle import color

from numpy import product




def BuyMe(prefix = 'Please buy me', what = 'something nice', *args, **kwargs):
    print(prefix, what)
    print(type(args), args)     # <class 'tuple'> ('a cat', 'a dog', 'a dragon')
    print(type(kwargs), kwargs) # <class 'dict'> {'shop': 'market', 'color': 'any'}

# BuyMe('Please buy me', 'new car', 'a cat', 'a dog', 'a dragon', shop = 'market', color = 'any')


products = ['milk', 'bread', 'flakes']
parameters = {'price':'low', 'time':'now'}

# BuyMe('Buy me', 'newspaper', products, parameters)
'''
Buy me newspaper
<class 'tuple'> (['milk', 'bread', 'flakes'], {'price': 'low', 'time': 'now'})
<class 'dict'> {}
'''

BuyMe('Buy me', 'newspaper', *products, **parameters)
'''
Buy me newspaper
<class 'tuple'> ('milk', 'bread', 'flakes')
<class 'dict'> {'price': 'low', 'time': 'now'}
'''