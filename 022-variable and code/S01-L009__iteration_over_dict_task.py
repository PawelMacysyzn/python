banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
list_of_zeros = [0] * len(banknotes_coins)

# {0.01: 0, 0.02: 0, 0.05: 0, 0.1: 0, 0.2: 0, 0.5: 0, 1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0, 200: 0, 500: 0}
dict_denominations = dict(zip(banknotes_coins, list_of_zeros))


dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1
 
dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2
 
dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for key in sorted(dict_denominations.keys()):
    print('Denomination: {0:6.2f} : {1:5}'.format(key, dict_denominations[key]))
'''
Denomination:   0.01 :     0
Denomination:   0.02 :     0
Denomination:   0.05 :     0
Denomination:   0.10 :     0
Denomination:   0.20 :     0
Denomination:   0.50 :     1
Denomination:   1.00 :     0
Denomination:   2.00 :     3
Denomination:   5.00 :     2
Denomination:  10.00 :     0
Denomination:  20.00 :     3
Denomination:  50.00 :     2
Denomination: 100.00 :     2
Denomination: 200.00 :     0
Denomination: 500.00 :     0
'''

print('*'*50)

sum = 0

for key in sorted(dict_denominations.keys()):
    if dict_denominations[key] > 0:
        print('Denomination: {0:6.2f} : {1:5}'.format(key, dict_denominations[key]))
        sum += key * dict_denominations[key]

'''
Denomination:   0.50 :     1
Denomination:   2.00 :     3
Denomination:   5.00 :     2
Denomination:  20.00 :     3
Denomination:  50.00 :     2
Denomination: 100.00 :     2
'''

print('-'*25)
print("The sum is:",sum) # The sum is: 376.5