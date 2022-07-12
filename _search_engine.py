import os
import csv
import types
import sys
import itertools as it
from typing import List


def cmd_support() -> tuple:
    '''
    # Allows for cmd support
    # Example:
    py .\_search_engine.py --find 'looking_phrase'
                or
    py .\_search_engine.py -f 'looking_phrase'

    * return tuple(actual_path, serch_string)

    '''
    actual_path = os.getcwd()

    if len(sys.argv) <= 1:

        # os.getcwd() returns current working directory of a proces
        # zwraca bieżący katalog roboczy procesu
        serch_string = 'glob'

    else:

        if len(sys.argv) > 3:

            for e, each in enumerate(sys.argv):
                print("[arg: {}] {:10s} {} ".format(
                    e, sys.argv[e], type(sys.argv[e])))

            raise Exception('Too many arguments !')

        if sys.argv[1].lower() in ('--find','-f'):
            pass
        else:
            raise Exception("You must give the command '--find' or '-f' !")

        if not sys.argv[2].isnumeric():
            serch_string = sys.argv[2]

        else:
            raise Exception("The second argument must be 'type str' !")

    return (actual_path, serch_string)


def generate_files_by_walk(path, file_extension: str = '.py') -> types.GeneratorType:
    for dir_name, subdirs, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(file_extension):
                fullFileName = os.path.join(dir_name, filename)
                yield fullFileName


def generate_files_by_scandir(path, file_extension: str = '.py') -> types.GeneratorType:
    '''
    * path (str) to the starting directory
    '''
    for entry in os.scandir(path):

        if not entry.name.startswith('.'):

            if entry.is_dir():
                yield from generate_files_by_scandir(os.path.join(path, entry.name))

            elif entry.is_file():
                if entry.name.endswith(file_extension):
                    yield os.path.join(path, entry.name)


def grep_files(serch_string: str, files):
    '''
    # Searches locations for the specified string
    * serch_string (str) - specified string
    * files (List[str]) - searched locations
    '''
    try:
        for file in files:
            with open(file) as open_file:
                for line, line_of_file in enumerate(open_file.readlines()):
                    if serch_string in line_of_file.rstrip('\n'):
                        yield 'File "{}", line {}'.format(file, line+1)
    except Exception as exc:
        print(exc)


def save_row_to_csv(*args, name_file: str = 'test.csv'):

    with open(os.path.join(os.getcwd(), name_file), 'a', newline='') as file:

        # create the csv writer
        csvwriter = csv.writer(file, delimiter=';')

        # write a row to the csv file
        csvwriter.writerow([*args])


def save_the_lines_found_to_csv() -> None:
    '''
    # Saves all found files in lines for each method in a separate column 
    # Zapisuje wszystkie wyszukane pliki w wierszach dla kazdej metody w osobnej kolumnie
    '''

    open(os.path.join(os.getcwd(), 'test.csv'), "w").close()

    walk = generate_files_by_walk(actual_path)
    scandir = generate_files_by_scandir(actual_path)

    for e, (each_walk, each_scandir) in enumerate(it.zip_longest(walk, scandir, fillvalue='unknown')):
        save_row_to_csv(e+1, each_walk, each_scandir)


def print_the_lines_found(fun) -> None:
    for e, each in enumerate(fun):
        print(e+1, each)


actual_path, serch_string = cmd_support()


# save_the_lines_found_to_csv()
for each in grep_files(serch_string, generate_files_by_walk(actual_path)):
    # for each in grep_files(serch_string, generate_files_by_scandir(actual_path)):
    print(each)
