import os
import requests


def gen_get_files(path):
    '''
    * dir (str) -   path of catalog
    '''
    for dir in os.listdir(path):
        yield (os.path.join(path, dir))


def gen_get_file_lines(filename):
    with open(filename) as file:
        for line in file.readlines():
            yield (line.rstrip('\n'))


def check_webpage(url):
    try:
        x = requests.get(url)

        if not x.status_code == 200:
            return False
    except Exception as e:
        # print("eror: {}".format(e))
        return False
    else:
        return True


# path = r'C:\Users\pmacyszyn_adm\Documents\python\python\000-python_basics'


for file in gen_get_files('c:/temp/links_to_check'):
    for address in gen_get_file_lines(file):
        print("File: {}\nAddress: {}\nDoes it exist: {}".format(file, address, check_webpage(address)))
        print('-'*45)

'''
File: c:/temp/links_to_check\com.txt
Address: http://www.realpython.com/
Does it exist: True
---------------------------------------------
File: c:/temp/links_to_check\com.txt
Address: http://www.nonexistenturl.com/
Does it exist: True
---------------------------------------------
File: c:/temp/links_to_check\com.txt
Address: http://www.stackoverflow.com
Does it exist: True
---------------------------------------------
File: c:/temp/links_to_check\pl.txt
Address: http://www.wykop.pl/
Does it exist: True
---------------------------------------------
File: c:/temp/links_to_check\pl.txt
Address: http://www.ale-beka-jest-taki-adres.pl/
Does it exist: False
---------------------------------------------
File: c:/temp/links_to_check\pl.txt
Address: http://www.demotywatory.pl
Does it exist: True
---------------------------------------------
'''