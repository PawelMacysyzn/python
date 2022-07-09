import itertools as it

# mylist = ['a', 'b', 'c', 'd']

# for combinations in it.combinations_with_replacement(mylist, 3):
#     print(combinations)

'''
money = [20, 20, 20, 20, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
results = list()

for i in range(1, 100+1):
    for combinations in it.combinations(money, i):
        if sum(combinations) == 100:
            results.append(combinations)

results = set(results)

for result in results:
    print(result)
''' 


money = [50, 20, 10, 5, 1]

e = 0
for i in range(1, 100+1):
    for combinations in it.combinations_with_replacement(money, i):
        if sum(combinations) == 100:
            e += 1
            print(e, combinations)

    
    
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    