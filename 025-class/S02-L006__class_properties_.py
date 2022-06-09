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

    '''
    # New property for class (
    #   a method that allows you to get values,
    #   method used to change the value,
    #   method that removes the attribute,
    #   documentation for this property)
    '''
    IsOnSale = property(GetIsSale, SetOnSale, None, 'if set to true, the car is availble in sale/promo')



car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)

 
print('Status of cars:', car_01.GetIsSale(), car_02.GetIsSale()) # Status of cars: False True
car_01.SetOnSale(True)  # Cannot change status IsOnSale. Sale valid only for Opel
car_02.SetOnSale(False) # Changing status IsOnSale to False for Opel
print('Status of cars:', car_01.GetIsSale(), car_02.GetIsSale()) # Status of cars: False False

# -------------------------------------------------------
print('-'*55)
# Status of cars: False False
print('Status of cars:', car_01.IsOnSale, car_02.IsOnSale)
car_01.IsOnSale = False # Cannot change status IsOnSale. Sale valid only for Opel
car_02.IsOnSale = True # Changing status IsOnSale to True for Opel

