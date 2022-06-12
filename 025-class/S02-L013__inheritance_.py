brandOnSale = 'Opel'


class Car(object):

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

    def IsDamaged(self): return not (
        self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print('{} {}'.format(self.brand, self.model).upper())
        print('Air Bag  - ok -     {}'.format(self.isAirBagOK))
        print('Painting - ok -     {}'.format(self.isPaintingOK))
        print('Mechanic - ok -     {}'.format(self.isMechanicOK))
        print('IS ON SALE          {}'.format(self.__isOnSale))
        print('-'*35)

    def __GetIsSale(self):
        return self.__isOnSale

    def __SetOnSale(self, newIsOnSalesStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSalesStatus
            print('Changing status IsOnSale to {} for {}'.format(
                newIsOnSalesStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(
                brandOnSale))

    IsOnSale = property(__GetIsSale, __SetOnSale, None,
                        'if set to true, the car is availble in sale/promo')
