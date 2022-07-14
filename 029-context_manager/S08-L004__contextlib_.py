from certifi import where


class Door:

    def __init__(self, where) -> None:
        self.where = where

    def open(self):
        print('Opening door to the {}'.format(self.where))

    def close(self):
        print('Closing door to the {}'.format(self.where))


# door1 = Door('hell')
# door2 = Door('future')

# door1.open()
# door1.close()
# door2.open()
# door2.close()

'''
Opening door to the hell
Closing door to the hell
Opening door to the future
Closing door to the future
'''

#-------------------------------------
'''
from contextlib import contextmanager

@contextmanager
def OnlyClose(obj):
    yield obj
    door.close()



with OnlyClose(Door('next room')) as door:
    door.open()
    print('the dore is to the {}'.format(door.where))



# Opening door to the next room
# the dore is to the next room
# Closing door to the next room

'''
#-------------------------------------
'''

# The closing function calls the close () method for the passed object
# Funkcja closing wywoluje dla przekazanego obiektu metodę close()

from urllib.request import urlopen
from contextlib import closing

with closing(urlopen('http://www.kursyonline24.eu')) as page:
    for line in page:
        print(line) # print contend of www
'''
 #-------------------------------------
# Ignoring the error
# Ignorowanie bledu

# import os
# # os.remove(r'C:\Users\pmacyszyn_adm\Documents\python\python\test.py')
        
# from contextlib import suppress
# with suppress(FileNotFoundError):
#     os.remove(r'C:\Users\pmacyszyn_adm\Documents\python\python\test.py')

#-------------------------------------

# Write screen output to file
# Zapisuje wyjscie z ekranu na plik

from contextlib import redirect_stdout
f =open(r'c:\temp\log.txt', 'w')
with redirect_stdout(f):
    print('Hello')       
    d = Door('Hello')
    d.open()
    d.close()
        
# All content is written to the file *log.txt   
        
        
