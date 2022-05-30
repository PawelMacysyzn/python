var_x = 10 
password = 'My super secret password'

source = 'password'
result = eval(source)
print(result) # My super secret password


source = 'var_x + 2'
result = eval(source)
print(result) # 12
#-------------------------------------------

'''
 {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x00000250C2564700>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:\\Users\\pmacyszyn_adm\\Documents\\python\\python\\023-code expansion\\S01-L013__eval.py', '__cached__': None, 'var_x': 10, 'password': 'My super secret password', 'source': 'var_x + 2', 
'result': 12}
'''
# print(globals())
#-------------------------------------------

source = 'password'

globals = globals().copy()

result = eval(source, globals)
print(result) # My super secret password

del globals[source]
result = eval(source, globals)
print(result) # NameError: name 'password' is not defined