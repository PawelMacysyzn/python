import os
import types
from typing import List


def scantree(path: str) -> types.GeneratorType:
    '''
    * path (str) to the starting directory
    '''
    for entry in os.scandir(path):

        if not entry.name.startswith('.'):

            if entry.is_dir():
                yield from scantree(os.path.join(path, entry.name))

            elif entry.is_file():
                yield os.path.join(path, entry.name)

def grep_files(serch_string: str, files):
    '''
    # Searches locations for the specified string
    * serch_string (str) - specified string
    * files (List[str]) - searched locations
    '''
    for file in files:
        with open(file) as text:
            if serch_string in text.read():
                yield file


actual_path = os.getcwd()
serch_string = 'typing'

file_generator = scantree(actual_path)


for e, each in enumerate(file_generator):
    print(e+1, each)


# Did not work #
'''
# for each in grep_files(serch_string, file_generator):
#     print(each)

'''
