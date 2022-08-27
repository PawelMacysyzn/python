import os

# current working directory
dir = os.path.abspath(os.getcwd())

def wrapper_with_parameters(log_action):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):

            print('-'*25)

            return func(*args, **kwargs)

        return inner_wrapper
    return wrapper


@wrapper_with_parameters
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")

@wrapper_with_parameters
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(os.path.join(dir, 'dummy_file.txt'))
delete_file(os.path.join(dir, 'dummy_file.txt'))
create_file(os.path.join(dir, 'dummy_file.txt'))
delete_file(os.path.join(dir, 'dummy_file.txt'))
