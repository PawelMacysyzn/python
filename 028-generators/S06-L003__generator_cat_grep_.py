import os 


path = r'C:\Users\pmacyszyn_adm\Documents\python\python\025-class'
serch_string = 'Ford'
file_extension = '.py'

for dir_name, subdirs, filenames in os.walk(path):
    # print(dir_name, subdirs, filenames)
    for filename in filenames:
        if filename.endswith(file_extension):
            fullFileName = os.path.join(dir_name, filename)
            for line in open(fullFileName):
                if serch_string in line:
                    print(filename)


'''
S02-L011__decorating_with_class_.py
S02-L013__inheritance_.py
S02-L013__inheritance_.py
'''

def generate_files(base_dir, file_extension):
    for dir_name, subdirs, filenames in os.walk(base_dir):
        for filename in filenames:
            if filename.endswith(file_extension):
                fullFileName = os.path.join(dir_name, filename)    
                yield fullFileName


def grep_files(serch_string, files):
    for file in files:
        with open(file) as text:
            if serch_string in text.read():
                yield file


file_generator = generate_files(path, file_extension)


for file in grep_files(serch_string, file_generator):
    print(file)


# '''
# C:\Users\pmacyszyn_adm\Documents\python\python\025-class\S02-L011__decorating_with_class_.py
# C:\Users\pmacyszyn_adm\Documents\python\python\025-class\S02-L013__inheritance_.py
# '''











