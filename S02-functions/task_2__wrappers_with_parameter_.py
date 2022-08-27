import os
import datetime



dir = os.path.abspath(os.getcwd())


'''
    Action FILE_CREATE executed on c:\temp\dummy_file.txt on 2029-01-12 9:29:17
'''

def wrapper_with_log_action(catalog_dir):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):


            action = change_function_for_text(func)
            path = os.path.join(dir, action) + '.txt'
            now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            log_end = '\n' + '-' * 25 + '\n'
            log = 'Action {} executed on {} on {} {}'.format(action, *args, now, log_end)

            with open(path, 'a') as f:
                f.write(log) 



            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper



@wrapper_with_log_action(dir)
def create_file(path):
    print('creating file {}'.format(path))
    open(path,"w+")
 
@wrapper_with_log_action(dir)
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)

def change_function_for_text(func):
    result = func.__name__.upper().split('_')
    result.reverse()
    return '_'.join(result)
 
 
create_file(os.path.join(dir, 'dummy_file.txt'))
delete_file(os.path.join(dir, 'dummy_file.txt'))
create_file(os.path.join(dir, 'dummy_file.txt'))
delete_file(os.path.join(dir, 'dummy_file.txt'))







