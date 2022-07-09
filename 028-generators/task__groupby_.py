import os, itertools
import types



def scantree(path: str):
    '''
    * path (str) to the starting directory
    '''
    for entry in os.scandir(path):

        if not entry.name.startswith('.') and entry.is_dir():
            yield {'type':True,'name':os.path.join(path, entry.name)}
            yield scantree(os.path.join(path, entry.name))

        elif not entry.name.startswith('.') and entry.is_file():
            yield {'type':False,'name':os.path.join(path, entry.name)}

listing = scantree(r'C:\Users\pmacyszyn_adm\Documents\python\python')

for obj in listing:

    if isinstance(obj, types.GeneratorType):
        for o in obj:
            print(o)
    else:
        print(obj)





















