import csv
 
with open('c:/TEMP/data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print('|'.join(row))


    while(True):
        try:
            print(csvreader.__next__())
        except StopIteration: break

'''
['Pharma A', ' Vitamin C', '100']
['Drugstore XYZ', 'Penicilin', ' 20', ' pills']
['Drugstore ABC', 'Aspirin', '60']
['Pharma X', 'Montelukast', '10']
'''