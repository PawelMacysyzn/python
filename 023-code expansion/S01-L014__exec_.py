from ast import expr


var_x = 10 

source = 'var_x = 2'
'''
result = eval(source)
print(result) # SyntaxError: invalid syntax
'''

result = exec(source)
print(result) # None

print(source, type(source)) # var_x = 2 <class 'str'>


source = '''
for i in range(var_x):
    print(i)
'''
print(source)
'''
for i in range(var_x):
    print(i)
'''

source_variable = "nev_var = 5"
exec(source_variable)
print(nev_var) # 5