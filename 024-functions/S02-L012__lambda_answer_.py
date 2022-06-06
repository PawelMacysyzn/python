menu = ['1:burger', '2:cola', '3:chips', '4:sauce']


def split_list(list):

    retlist = []

    for s in list:
        retlist.append(s.split(':')[1])
    return retlist

print(split_list(menu))     # ['burger', 'cola', 'chips', 'sauce']

print(list(map(lambda x: x.split(':')[1],menu)))   # ['burger', 'cola', 'chips', 'sauce']

print(list(map(lambda x: print(x.split(':')[1]), menu)))
'''
burger
cola
chips
sauce
[None, None, None, None]
'''
list(map(lambda x: print(x.split(':')[1]), menu))  
'''
burger
cola
chips
sauce
'''
