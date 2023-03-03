##################################################################
# a program designed for name renaming of files
# File is used to rename the file in the selected location (PATH)
##################################################################

from hashlib import new
import os

##################################################################

PATH = r'C:\Users\pmacyszyn_adm\Documents\HTML_CSS_JS\HTML_CSS_JS\x_ATOTECH\GENERATED REPORT\REPORTS'
FIND = 'Style.js'
REPLACE = 'Style.xml'

##################################################################


def change_file_name_in_dir(path, find, replace):

    change_counter = 0

    CYELLOW = '\033[93m'
    CEND = '\033[0m'

    for root, old_name in get_file_name_by_yeld(path):

        new_name = replace_name(old_name, find, replace)

        old_path_name = os.path.join(root, old_name)
        new_path_name = os.path.join(root, new_name)

        change_counter += rename_file(old_path_name, new_path_name)

    if change_counter:
        print("{}Number of files changed: {}{}".format(
            CYELLOW, change_counter, CEND))
    else:
        print("{}None of files changed: {}".format(CYELLOW, CEND))


def replace_name(bace, find, replace):
    return bace.replace(find, replace)


def get_file_name_by_yeld(path):
    for root, dirs, files in os.walk(path):
        for file_name in files:
            yield (root, file_name)


def rename_file(old_path_name, new_path_name):
    CRED = '\033[91m'
    CGREEN = '\033[92m'
    CEND = '\033[0m'

    try:
        os.rename(old_path_name, new_path_name)
    except FileNotFoundError:
        print(CRED + "Oops! This file does not exist, check name.." + CEND)
    else:
        if old_path_name != new_path_name:
            print(CGREEN + "File name successfully changed" + CEND)
            return 1
        return 0


def test_print_files_but_with_replace_name(path):
    for root, name in get_file_name_by_yeld(path):
        print(os.path.join(root, replace_name(name, FIND, REPLACE)))


def main():

    # test_print_files_but_with_replace_name(PATH) # test

    # program
    change_file_name_in_dir(PATH, FIND, REPLACE)


if __name__ == '__main__':
    main()
