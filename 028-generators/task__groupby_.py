import os
import itertools as it
import types


def scantree(path: str):
    '''
    * path (str) to the starting directory
    '''
    for entry in os.scandir(path):

        if entry.is_dir():
            yield {'type': True, 'path': os.path.join(path, entry.name)}
            yield from scantree(os.path.join(path, entry.name))

        elif entry.is_file():
            yield {'type': False, 'path': os.path.join(path, entry.name)}


listing = scantree(r'C:\Users\pmacyszyn_adm\Documents\python\python')

listing = sorted(listing, key=lambda x: x['type'])


def scantree_print_elements(list: types.GeneratorType) -> None:
    for e, element in enumerate(list):
        if isinstance(element, types.GeneratorType):
            scantree_print_elements(element)
        else:
            print('[{:3d}] {:4s} - {}'.format(e+1,
                  'Dir' if element['type'] else 'File', element['path']))


scantree_print_elements(listing)

# '''
# [  1] File - C:\Users\pmacyszyn_adm\Documents\python\python\.git\.COMMIT_EDITMSG.swp
# [  2] File - C:\Users\pmacyszyn_adm\Documents\python\python\.git\COMMIT_EDITMSG
#                                     ...
# [703] Dir  - C:\Users\pmacyszyn_adm\Documents\python\python\threading
# [704] Dir  - C:\Users\pmacyszyn_adm\Documents\python\python\to_do_list
# '''

for key, elements in it.groupby(listing, key=lambda x: x['type']):
    print('The Quantity of {:8s}: {}'.format(
        'Catalogs' if key else 'Files', len(list(elements))))
