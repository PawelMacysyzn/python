class Car():

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self): return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print('{} {}'.format(self.brand, self.model).upper())
        print('Air Bag  - ok -     {}'.format(self.isAirBagOK))
        print('Painting - ok -     {}'.format(self.isPaintingOK))
        print('Mechanic - ok -     {}'.format(self.isMechanicOK))
        print('IS ON SALE          {}'.format(self.__isOnSale))
        print('-'*35)


car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)


car_02.__isOnSale = False # does not work
car_02.GetInfo()
'''
OPEL CORSA
Air Bag  - ok -     True
Painting - ok -     False
Mechanic - ok -     True
IS ON SALE          True
-----------------------------------
'''

print(vars(car_02)) # '__isOnSale': False} 
'''
{'brand': 'Opel', 'model': 'Corsa', 'isAirBagOK': True, 'isPaintingOK': False, 'isMechanicOK': True, '_Car__isOnSale': True, '__isOnSale': False}  
'''
car_02._Car__isOnSale = False 
car_02.GetInfo() # IS ON SALE          False

# ---------------------------------------------------------

car_02.YearOfProdution = 2005
print(vars(car_02))
'''
{'brand': 'Opel', 'model': 'Corsa', 'isAirBagOK': True, 'isPaintingOK': False, 'isMechanicOK': True, '_Car__isOnSale': False, '__isOnSale': False, 
'YearOfProdution': 2005}
'''
del car_02.YearOfProdution
print(vars(car_02))
'''
{'brand': 'Opel', 'model': 'Corsa', 'isAirBagOK': True, 'isPaintingOK': False, 'isMechanicOK': True, '_Car__isOnSale': False, '__isOnSale': False}
'''

# ---------------------------------------------------------

setattr(car_02, 'TAXI', False)
print(vars(car_02)) # ... 'TAXI': False}

print(hasattr(car_02, 'TAXI')) # True

delattr(car_02, 'TAXI')
print(hasattr(car_02, 'TAXI')) # False

# ---------------------------------------------------------
