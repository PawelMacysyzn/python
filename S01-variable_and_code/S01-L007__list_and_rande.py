# for i in range(10,0,-1):
#     print(i)

my_list = range(10)

print("my_list: ",type(my_list)) # my_list:  <class 'range'>

my_list = list(my_list)

print("my_list: ",type(my_list)) # my_list:  <class 'list'>

print("--"*36)

print(my_list[:])          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[1:])         # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[:6])         # [0, 1, 2, 3, 4, 5]
print(my_list[:-2])        # [0, 1, 2, 3, 4, 5, 6, 7]
print(my_list[5:7])        # [5, 6]
print(my_list[5:])         # [5, 6, 7, 8, 9]
print(my_list[5:-2])       # [5, 6, 7]
print(my_list[-3:])        # [7, 8, 9]
print(my_list[-3:-2])      # [7]
print(my_list[-1:0:-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(my_list[-1::-1])     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


print("--"*36)

# my_list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - <class 'list'> id[3191550344192]
print("my_list: {} - {} id[{}]".format(my_list[:],type(my_list), id(my_list)))


# copy() new hint

new_list = my_list[:] # or new_list = list.copy()

# my_list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - <class 'list'> id[3191550111680]
print("my_list: {} - {} id[{}]".format(new_list[:],type(new_list), id(new_list)))


#-----------------------------------------------------------------------------------------
 