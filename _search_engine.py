import os, csv
import types
import itertools as it
from typing import List


def generate_files_by_walk(path, file_extension: str = '.py'):
    for dir_name, subdirs, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(file_extension):
                fullFileName = os.path.join(dir_name, filename)
                yield fullFileName


def generate_files_by_scandir(path: str) -> types.GeneratorType:
    '''
    * path (str) to the starting directory
    '''
    for entry in os.scandir(path):

        if not entry.name.startswith('.'):

            if entry.is_dir():
                yield from generate_files_by_scandir(os.path.join(path, entry.name))

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


def save_row_to_csv(*args, name_file: str = 'test.csv'):

    with open(os.path.join(os.getcwd(), name_file), 'a', newline='') as file:

        # create the csv writer
        csvwriter = csv.writer(file, delimiter=';')


        # write a row to the csv file
        csvwriter.writerow([*args])
        




actual_path = os.getcwd()
serch_string = ['typing']




open(os.path.join(os.getcwd(), 'test.csv'), "w").close()

walk = generate_files_by_walk(actual_path)
scandir = generate_files_by_scandir(actual_path)

for e, (each_walk, each_scandir) in enumerate(it.zip_longest(walk, scandir, fillvalue= 'unknown')):
    # print(e+1, each_walk, each_scandir)
    save_row_to_csv(e+1, each_walk, each_scandir)





# Did not work #
'''
# for each in grep_files(serch_string, file_generator):
#     print(each)

'''
