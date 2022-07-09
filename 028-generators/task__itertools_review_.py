import itertools as it


def get_factors(x) -> list:
 
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list

def get_stuff(list: list) -> str:
    list_str = ''
    for e, each in enumerate(list):
        if e: list_str += ' + '
        list_str += str(each)
    return list_str

# print(sum(get_factors(20)))


candidate_list = list(range(1, 1000+1))
filtered_list = list()


for number in it.filterfalse(lambda x: x != sum(get_factors(x)), candidate_list):
    filtered_list.append(number)

for number in filtered_list:
    print('{:<3d} = {}'.format(number, get_stuff(get_factors(number))))

'''
6   = 1 + 2 + 3
28  = 1 + 2 + 4 + 7 + 14
496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248
'''


