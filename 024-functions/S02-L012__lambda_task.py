text_list = ['x','xxx','xxxxx','xxxxxxx','']


f = lambda str: len(str)


print(f(text_list))     # 5


print(list(map(f, text_list)))  # [1, 3, 5, 7, 0]


print(list(map(lambda str: len(str), text_list)))   # [1, 3, 5, 7, 0]