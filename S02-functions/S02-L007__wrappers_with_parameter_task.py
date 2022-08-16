import os, functools
from datetime import datetime as dt
 

def wrapper_with_log_file(logged_action, log_file_path):

    def wrapper_with_log_to_known_file(func):

        def the_real_wrapper(path):

            file = open(log_file_path,'a')
            file.write('-'*20 + '\n')
            file.write('Action {} executed on {} on {}\n'.format(logged_action, path, dt.now().strftime("%Y-%m-%d %H:%M:%S")))
            file.close()

            return func(path)

        return the_real_wrapper

    return wrapper_with_log_to_known_file


@wrapper_with_log_file('FILE_CREATE', r'c:/temp/file_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    with open(path,"w+") as f:
        f
   
 
@wrapper_with_log_file('FILE_DELETE', r'c:/temp/file_delete.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)
 
 
create_file(r'c:\temp\dummy_file.txt')
delete_file(r'c:\temp\dummy_file.txt')
create_file(r'c:\temp\dummy_file.txt')
delete_file(r'c:\temp\dummy_file.txt')

#in cmd:
'''
creating file c:\temp\dummy_file.txt
deleting file c:\temp\dummy_file.txt
creating file c:\temp\dummy_file.txt
deleting file c:\temp\dummy_file.txt
'''
# in file file_create.txt:
'''
--------------------
Action FILE_CREATE executed on c:\temp\dummy_file.txt on 2022-06-03 12:52:49
--------------------
Action FILE_CREATE executed on c:\temp\dummy_file.txt on 2022-06-03 12:52:49

'''
# in file file_delete.txt
'''
--------------------
Action FILE_DELETE executed on c:\temp\dummy_file.txt on 2022-06-03 12:52:49
--------------------
Action FILE_DELETE executed on c:\temp\dummy_file.txt on 2022-06-03 12:52:49

'''