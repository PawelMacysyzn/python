class Car:

    def __init__(self, brand, model, isOnSale):
        print('>> Class Car - init - starting')
        self.brand = brand
        self.model = model
        self.isOnSale = isOnSale
        print('>> Class Car - init - sropping')

    def GetInfo(self):
        print('>> Class Car - GetInfo - starting')
        super().GetInfo()
        print('{} {}'.format(self.brand, self.model).upper())
        print('IS ON SALE          {}'.format(self.isOnSale))
        print('>> Class Car - GetInfo - sropping')

class Specialist:

    def __init__(self, firstname, lastname, brand):
        print('>> Class Specialist - init - starting')
        self.firstname = firstname
        self.lastname = lastname
        self.name = '{} {}'.format(firstname, lastname)
        self.brand = brand
        print('>> Class Specialist - init - sropping')

    def GetInfo(self):
        print('>> Class Specialist - GetInfo - starting')
        print('{} {} - ({})'.format(self.firstname, self.lastname, self.brand))
        print('>> Class Specialist - GetInfo - sropping')

class CarSpecialist(Car, Specialist):

    def __init__(self, brand, model, isOnSale, firstname, lastname):
        print('>> Class CarSpecialist - init - starting')
        Car.__init__(self, brand, model, isOnSale)
        Specialist.__init__(self, firstname, lastname, brand.upper())
        print('>> Class CarSpecialist - init - sropping')

    def GetInfo(self):
        print('>> Class CarSpecialist - GetInfo - starting')
        super().GetInfo()
        print('>> Class CarSpecialist - GetInfo - sropping')



tom = CarSpecialist('Toyota', 'Corolla', True, 'Tom', 'Smith')
print(vars(tom))
'''
>> Class CarSpecialist - init - starting
    >> Class Car - init - starting       
    >> Class Car - init - sropping       
    >> Class Specialist - init - starting
    >> Class Specialist - init - sropping
>> Class CarSpecialist - init - sropping
{'brand': 'TOYOTA', 'model': 'Corolla', 'isOnSale': True, 'firstname': 'Tom', 'lastname': 'Smith', 'name': 'Tom Smith'}
'''

tom.GetInfo()
'''
>> Class CarSpecialist - GetInfo - starting
    >> Class Car - GetInfo - starting
        >> Class Specialist - GetInfo - starting

        Tom Smith - (TOYOTA)

        >> Class Specialist - GetInfo - sropping

    TOYOTA COROLLA
    IS ON SALE          True

    >> Class Car - GetInfo - sropping
>> Class CarSpecialist - GetInfo - sropping
'''


#Method Resolution Order
print(CarSpecialist.__mro__)
'''
(<class '__main__.CarSpecialist'>, <class '__main__.Car'>, <class '__main__.Specialist'>, <class 'object'>)
'''



# MRO - method resolution order  !