import itertools as it


filepath = r'C:\Users\pmacyszyn_adm\Documents\python\python\028-generators\data.txt'


data = list()

with open(filepath) as file:

    for line in file:
        elements = line.rstrip('\n').split(':')
        d = {'type' : elements[0], 'action' : elements[1]}
        data.append(d)


for dat in data:
    # print(dat)
    pass

data = sorted(data, key= lambda x: x['type'])


for key, elements in it.groupby(data, key = lambda x: x['type']):
    print('The key is {} and the number of elements is {}'.format(key, len(list(elements))))


'''
The key is ACTION and the number of elements is 3
The key is ALARM and the number of elements is 6
The key is ERROR and the number of elements is 3
'''























