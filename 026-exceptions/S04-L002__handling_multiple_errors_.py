from decimal import DivisionByZero


clients = {
    "INFO": 0.5,
    "DATA": 0.2,
    "SOFT": 0.2,
    "INTER": 0.1,
    "OMEGA": 0.0
}

myClient = input("Enter client's name: ").upper()
totalCost = 7200

try:
    ratio = float(input('Enter new ratio: '))
    print("The default % ratio for {} is {}, a new one is {}".format(myClient, clients[myClient], ratio))
    print('The cost for {} is {}'.format(myClient, ratio * totalCost))
    print('The new ratio in comparison to old ratio: {}'.format(clients[myClient]/ratio))


except KeyError as e:
    print('Client {} is not on list {}.\nDetails:\n{}'.format(myClient, [client for client in clients.keys()], e))

except (ValueError, ZeroDivisionError) as e:
    print('There is a problem with entered value for ratio - is must be a number greater than 0.\nDetails:\n{}'.format(e))

# except ZeroDivisionError as e:
#     print('The new ratio cannot be 0.\nDetails:\n{}'.format(e))

except Exception as e:
    print("Sorry we have an error...\nDetails:\n{}".format(e))


'''
Enter client's name: info
Enter new ratio: 0.3
The default % ratio for INFO is 0.5, a new one is 0.3
The cost for INFO is 2160.0
The new ratio in comparison to old ratio: 1.6666666666666667
'''
