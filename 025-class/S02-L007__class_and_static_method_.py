brandOnSale = 'Opel'


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

    def GetIsSale(self):
        return self.__isOnSale

    def SetOnSale(self, newIsOnSalesStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSalesStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSalesStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))

    IsOnSale = property(GetIsSale, SetOnSale, None, 'if set to true, the car is availble in sale/promo')

    @classmethod
    def ReadFromText(cls, aText):
        aNewCar = cls(*aText.split(':'))
        return aNewCar
    
    @staticmethod
    def Convert_KM_KW(KM):
        return KM * 0.735

    @staticmethod
    def Convert_KW_KM(KW):
        return KW * 1.36
    

# car_01 = Car('Seat', 'Ibiza', True, True, True, False)
# car_02 = Car('Opel', 'Corsa', True, False, True, True)

lineOfText = 'Renault:Megane:True:True:False:False'
car_03 = Car.ReadFromText(lineOfText)

car_03.GetInfo()
'''
RENAULT MEGANE
Air Bag  - ok -     True  
Painting - ok -     True 
Mechanic - ok -     False
IS ON SALE          False
-----------------------------------'''


print('Converting 120 KM to KW', Car.Convert_KM_KW(120))
print('Converting 90 KW to KM', Car.Convert_KW_KM(90))
'''
Converting 120 KM to KW 88.2
Converting 90 KW to KM 122.4
'''

# print(Car.GetInfo()) # TypeError: Car.GetInfo() missing 1 required positional argument: 'self'

print(car_03.ReadFromText(lineOfText)) # <__main__.Car object at 0x0000022B7D713C70>
print(car_03.Convert_KM_KW(39)) # 28.665