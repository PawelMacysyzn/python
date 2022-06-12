class Car():

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, accessories):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.accessories = accessories

    def GetInfo(self):
        print('{} {}'.format(self.brand, self.model).upper())
        print('Air Bag  - ok -     {}'.format(self.isAirBagOK))
        print('Painting - ok -     {}'.format(self.isPaintingOK))
        print('Mechanic - ok -     {}'.format(self.isMechanicOK))
        print('Accessories         {}'.format(self.accessories))
        print('-'*35)

    def __iadd__(self, other):
        if type(other) is list:
            accessories = self.accessories
            # print('self.accessories:', id(self.accessories)) # self.accessories: 2181143581440
            # print('accessories:', id(accessories))           # accessories:      2181143581440
            accessories.extend(other)
            return Car(self.brand, self.model, self.isAirBagOK, self.isPaintingOK,
                       self.isMechanicOK, accessories)
        elif type(other) is str:
            accessories = self.accessories
            accessories.append(other)
            return Car(self.brand, self.model, self.isAirBagOK, self.isPaintingOK,
                       self.isMechanicOK, accessories)
        else:
            raise Exception(
                'Adding type {} to Car is not implemented'.format(type(other)))

    def __add__(self, other):
        if type(other) is Car:
            return [self, other]
        else:
            raise Exception(
                'Adding type {} to Car is not implemented'.format(type(other)))

    def __str__(self) -> str:
        return "Brand: {}, Model: {}".format(self.brand, self.model)
    


car_01 = Car('Seat', 'Ibiza', True, True, True, ['winter tires'])
car_01.GetInfo()

car_01 += ['navigation system', 'roof rack']
car_01.GetInfo()


car_01 += 'loudspeeker system'
car_01.GetInfo()

car_02 = Car('Opel', 'Corsa', True, False, True, [])
car_02.GetInfo()


car_pack = car_01 + car_02
print('car_01 + car_02 =',car_pack[0].brand, car_pack[1].brand)

print(type(car_pack)) # <class 'list'>


print(car_01)
'''
Before:
<__main__.Car object at 0x0000024FFED93FD0>

Now:
Brand: Seat, Model: Ibiza
'''

car_01 += 'supe','gum'