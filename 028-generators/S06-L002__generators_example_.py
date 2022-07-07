
# file = open(r'028-generators\data.txt')
# data = file.read()
# file.close()

#------------------------------------------

# for line in data.splitlines():
#     if line.startswith('ACTION'):
#         print(line)

#------------------------------------------

# with open(r'028-generators\data.txt') as file:
#     for line in file:
#         if line.startswith('ACTION'):
#             print(line.replace('\n', ''))

#------------------------------------------

# file = open(r'028-generators\data.txt')

# for line in file:
#     if line.startswith('ACTION'):
#         print(line.replace('\n', ''))
# file.close()

#------------------------------------------

# file = open(r'028-generators\data.txt')

# records = list()

# for line in file:
#     if ':' in line:
#         type, action = line.rstrip('\n').split(':', 1)
#         record = (type, action.strip()) 
#         records.append(record)

# file.close()

#------------------------------------------

def get_records(filePath: str):
    print('---opening file---')

    file = open(filePath)


    for line in file:
        if ':' in line:
            type, action = line.rstrip('\n').split(':',1)
        record = (type, action.strip())
        yield record 


    print('---closing file---')
    file.close()



for record in get_records(r'028-generators\data.txt'):
    print('The type is {} and the action is {}'.format(record[0],record[1]))

'''
---opening file---
The type is ALARM and the action is WAITING FOR JOB
The type is ALARM and the action is WAITING FOR JOB
The type is ERROR and the action is TIMEOUT
The type is ACTION and the action is GET STATUS
The type is ALARM and the action is WAITING FOR STATUS
The type is ALARM and the action is WAITING FOR STATUS
The type is ERROR and the action is TIMEOUT
The type is ACTION and the action is GET STATUS
The type is ALARM and the action is WAITING FOR STATUS
The type is ALARM and the action is WAITING FOR STATUS
The type is ERROR and the action is TIMEOUT
The type is ACTION and the action is CALL OPERATOR
---closing file---
'''








