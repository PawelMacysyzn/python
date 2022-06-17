brandOnSale = 'Opel'


class Car(object):

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        print('>>> This is __init__ of parent class:', self.__class__.__name__)
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


class Truck(Car):

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale, capacityKg):
        print('>>> This is __init__ of child class:', self.__class__.__name__)
        # super(Truck, self).__init__(brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale)
        # super().__init__(brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale)
        Car.__init__(self, brand, model, isAirBagOK,
                     isPaintingOK, isMechanicOK, isOnSale)
        self.capacityKg = capacityKg

    def GetInfo(self):
        print('CapacityKg   -   {}'.format(self.capacityKg))
        super().GetInfo()


truck_01 = Truck('Ford', 'Transit', True, False, True, False, 1600)
truck_02 = Truck('Reanult', 'Trafic', True, True, True, True, 1200)


print('Calling properties:')
print(truck_01.brand, truck_01.capacityKg, truck_01.IsOnSale,
      truck_02.brand, truck_02.capacityKg, truck_02.IsOnSale)

truck_01.GetInfo()
truck_02.GetInfo()


'''
>>> This is __init__ of child class: Truck
>>> This is __init__ of parent class: Truck
>>> This is __init__ of child class: Truck
>>> This is __init__ of parent class: Truck
Calling properties:
Ford 1600 False Reanult 1200 True
CapacityKg   -   1600
FORD TRANSIT
Air Bag  - ok -     True
Painting - ok -     False
Mechanic - ok -     True
IS ON SALE          False
-----------------------------------
CapacityKg   -   1200
REANULT TRAFIC
Air Bag  - ok -     True
Painting - ok -     True
Mechanic - ok -     True
IS ON SALE          True
-----------------------------------
'''