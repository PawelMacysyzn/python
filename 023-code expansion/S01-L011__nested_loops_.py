
listA = list(range(6))
listB = list(range(6))

# [0, 1, 2, 3, 4, 5] [0, 1, 2, 3, 4, 5]
print(listA, listB)

product_list = [] 
# for a in listA:
#     for b in listB:
#         product_list.append((a,b))
 
# or

product_list = [(a,b) for a in listA for b in listB]
# [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]   
print(product_list)




product_list = [(a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0]
# [(1, 0), (1, 2), (1, 4), (3, 0), (3, 2), (3, 4), (5, 0), (5, 2), (5, 4)]
print(product_list)