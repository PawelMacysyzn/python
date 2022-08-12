import datetime
import functools


    # logFilePath = r'c:\temp\function_log.txt'

def CreateFunctionWithWrapper_logToFile(logFilePath):
    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args, **kwargs):
            file = open(logFilePath,'a')
            file.write('-'*20 + '\n')
            file.write('Function "{}" satrted at {}'.format(func.__name__, datetime.datetime.now().isoformat()))
            file.write('following arguments were used:' + '\n')
            file.write(" ".join('{}'.format(x) for x in args))
            file.write('\n')
            file.write(" ".join('{} = {}'.format(k,w) for k,w in kwargs.items()))
            file.write('\n')

            result = func(*args, **kwargs)

            file.write('Function returned {}\n'.format(result))
            file.close()
            return result
        return func_with_wrapper
    return CreateFunctionWithWrapper


@CreateFunctionWithWrapper_logToFile(r'c:\temp\function_salary_log.txt')
def ChangeSalary(emp_name, new_salary, is_bonus = False):
    print('CHANGING SALARY FOR {} TO {} AS BONUS={}'.format(emp_name, new_salary, is_bonus))
    return new_salary

@CreateFunctionWithWrapper_logToFile(r'c:\temp\function_position_log.txt')
def ChangePosition(emp_name, new_position):
    print('CHANGING position FOR {} TO {}'.format(emp_name, new_position))
    return new_position


print(ChangeSalary('Johnson', 20000, True))
print(ChangeSalary('Johnson', 20000, is_bonus = True))
print(ChangePosition('Michael', 'Salesman'))
print(ChangePosition('Anke', 'Manager'))

# in file function_position_log.txt
'''
--------------------
Function "ChangePosition" satrted at 2022-06-03T12:00:19.972853following arguments were used:
Michael Salesman

Function returned Salesman
--------------------
Function "ChangePosition" satrted at 2022-06-03T12:00:19.973853following arguments were used:
Anke Manager

Function returned Manager

'''
# in file function_salary_log.txt
'''
--------------------
Function "ChangeSalary" satrted at 2022-06-03T12:00:19.971857following arguments were used:
Johnson 20000 True

Function returned 20000
--------------------
Function "ChangeSalary" satrted at 2022-06-03T12:00:19.972853following arguments were used:
Johnson 20000
is_bonus = True
Function returned 20000

'''
# in cmd:
'''
CHANGING SALARY FOR Johnson TO 20000 AS BONUS=True
20000
CHANGING SALARY FOR Johnson TO 20000 AS BONUS=True
20000
CHANGING position FOR Michael TO Salesman
Salesman
CHANGING position FOR Anke TO Manager
Manager
'''