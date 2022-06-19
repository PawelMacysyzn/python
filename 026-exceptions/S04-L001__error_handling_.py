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
    print("The % ratio for {} is {}".format(myClient, clients[myClient]))
except Exception as e:
    print("Sorry we have an error...\nDetails:\n{}".format(e))
else:   #   perform if no error exist
    print("The cost for {} is {}".format(myClient, clients[myClient]*totalCost))
finally:#   perform always
    print("-= Calculation finished =-")

'''
Enter client's name: acs
Sorry we have an error...
Details:
'ACS'
-= Calculation finished =-
'''
