import math, time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

loops = 10000

argument_list = []
for i in range (loops):
    argument_list.append(i/10)



print('Results by non_compile_eval:')
print('='*45)
for formula in formulas_list:

    results_list = []
    print('{}'.format(formula))
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    stop = time.time()

    print('min: {1}    max: {0}'.format(max(results_list),min(results_list)))
    print('-'*40)
    print('Delta_time: {}'.format(stop - start))
    print('*'*45)
'''
Results by non_compile_eval:
=============================================
abs(x**3 - x**0.5)
min: 0.0    max: 999699998.3778045
----------------------------------------
Delta_time: 0.06398701667785645
*********************************************
abs(math.sin(x) * x**2)
min: 0.0    max: 994028.6327881699
----------------------------------------
Delta_time: 0.06798720359802246
*********************************************
'''
print()

print('Results by compile_eval:')
print('='*45)
for formula in formulas_list:

    results_list = []
    print('{}'.format(formula))
    start = time.time()
    sourceCompiled = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(eval(sourceCompiled))
    stop = time.time()

    print('min: {1}    max: {0}'.format(max(results_list),min(results_list)))
    print('-'*40)
    print('Delta_time: {}'.format(stop - start))
    print('*'*45)