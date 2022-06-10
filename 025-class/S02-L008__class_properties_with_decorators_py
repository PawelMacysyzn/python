brandOnSale = 'Opel'


class Car():

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale

    @property
    def IsOnSale(self):
        return self.__isOnSale

    @IsOnSale.setter
    def IsOnSale(self, newIsOnSalesStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSalesStatus
            print('Changing status IsOnSale to {} for {}'.format(
                newIsOnSalesStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(
                brandOnSale))

    @IsOnSale.deleter
    def IsOnSale(self):
        self.__isOnSale = None

    @property
    def CarTitle(self):
        return "Brand: {}, Model: {}".format(self.brand, self.model).title()


car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_01.IsOnSale = True  # possible to do
del car_01.IsOnSale
print(car_01.IsOnSale) # None
print(car_01.CarTitle) # Brand: Seat, Model: Ibiza


# or class property

'''

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

    #           property(_geter, _seter, _destructor, 'text')
    IsOnSale = property(__GetIsSale, __SetOnSale, None,
                        'if set to true, the car is availble in sale/promo')
    
car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_01.IsOnSale = True  # possible to do
'''
