import datetime
import functools


def CreateFunctionWithWrapper(func):
    def func_with_wrapper(*args, **kwargs):
        print('Function "{}" satrted at {}'.format(func.__name__, datetime.datetime.now().isoformat()))
        print('following arguments were used:')
        print(args, kwargs)
        result = func(*args, **kwargs)
        print('Function returned {}'.format(result))
        return result
    return func_with_wrapper

@CreateFunctionWithWrapper
def ChangeSalary(emp_name, new_salary, is_bonus = False):
    print('CHANGING SALARY FOR {} TO {} AS BONUS={}'.format(emp_name, new_salary, is_bonus))
    return new_salary

print(ChangeSalary('Johnson', 20000, is_bonus = True))
'''
Function "ChangeSalary" satrted at 2022-06-02T15:25:41.563598
following arguments were used:
('Johnson', 20000) {'is_bonus': True}
CHANGING SALARY FOR Johnson TO 20000 AS BONUS=True
Function returned 20000
20000
'''


def old_way():

    def ChangeSalary(emp_name, new_salary, is_bonus = False):
        print('CHANGING SALARY FOR {} TO {} AS BONUS={}'.format(emp_name, new_salary, is_bonus))
        return new_salary

    print(ChangeSalary('Johnson', 20000, True))
    '''
    CHANGING SALARY FOR Johnson TO 20000 AS BONUS=True
    20000
    '''
    # -----------------------------------------------------------
    """
    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args, **kwargs):
            print('-'*10)
            result = func(*args, **kwargs)
            print('+'*10)
            return result
        return func_with_wrapper

    ChangeSalaryWithWithLog = CreateFunctionWithWrapper(ChangeSalary)
    print(ChangeSalaryWithWithLog('Johnson', 20000, True))
    ''''
    ----------
    CHANGING SALARY FOR Johnson TO 20000 AS BONUS=True
    ++++++++++
    20000
    '''
    """
    # -----------------------------------------------------------
    print('*'*55)

    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args, **kwargs):
            print('Function "{}" satrted at {}'.format(func.__name__, datetime.datetime.now().isoformat()))
            print('following arguments were used:')
            print(args, kwargs)
            result = func(*args, **kwargs)
            print('Function returned {}'.format(result))
            return result
        return func_with_wrapper

    ChangeSalaryWithWithLog = CreateFunctionWithWrapper(ChangeSalary)
    print(ChangeSalaryWithWithLog('Johnson', 20000, is_bonus = True))
    '''
    Function "ChangeSalary" satrted at 2022-06-02T15:18:53.780267
    following arguments were used:
    ('Johnson', 20000) {'is_bonus': True}
    CHANGING SALARY FOR Johnson TO 20000 AS BONUS=True
    Function returned 20000
    20000
    ''' 

    # --------------------------------------------------------------
    print('*'*55)

    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args, **kwargs):
            print('Function "{}" satrted at {}'.format(func.__name__, datetime.datetime.now().isoformat()))
            print('following arguments were used:')
            print(args, kwargs)
            result = func(*args, **kwargs)
            print('Function returned {}'.format(result))
            return result
        return func_with_wrapper

    ChangeSalary = CreateFunctionWithWrapper(ChangeSalary)   # ChangeSalary !!!
    print(ChangeSalary('Johnson', 20000, is_bonus = True))
    '''
    Function "ChangeSalary" satrted at 2022-06-02T15:17:42.474440
    following arguments were used:
    ('Johnson', 20000) {'is_bonus': True}
    CHANGING SALARY FOR Johnson TO 20000 AS BONUS=True
    Function returned 20000
    20000
    ''' 

    # --------------------------------------------------------------
    print('*'*55)

# old_way()


