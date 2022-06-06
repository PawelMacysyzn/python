class Car():

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK

    def IsDamaged(self): return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print('{} {}'.format(self.brand, self.model))
        print('Air Bag  - ok -     {}'.format(self.isAirBagOK))
        print('Painting - ok -     {}'.format(self.isPaintingOK))
        print('Mechanic - ok -     {}'.format(self.isMechanicOK))
        print('-'*35)


car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)


print("Id of class is:",id(Car))
print('Id of instance are:', id(car_01), id(car_02))
'''
Id of class is: 2086751971520
Id of instance are: 2086761970416 2086761970320
'''

print('Check if object belongs to class:', isinstance(car_01, Car))
print('Check if object belongs to class using type:', type(car_01) is Car)
print('Check class of an object using __class__:', car_01.__class__)
'''
Check if object belongs to class: True
Check if object belongs to class using type: True
Check class of an object using __class__: <class '__main__.Car'>
'''

print('List of instance attributes with values:', vars(car_01))
# List of instance attributes with values: {'brand': 'Seat', 'model': 'Ibiza', 'isAirBagOK': True, 'isPaintingOK': True, 'isMechanicOK': True} 

print('List of class attributes with values:', vars(Car))
'''
List of class attributes with values:
 {'__module__': '__main__', 'numberOfCars': 0, 'listOfCars': [], '__init__':
  <function Car.__init__ at 0x000001C893DDAEF0>,
   'IsDamaged': <function Car.IsDamaged at 0x000001C893DDAF80>,
    'GetInfo': <function Car.GetInfo at 0x000001C893DDB010>,
     '__dict__': <attribute '__dict__' of 'Car' objects>,
      '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None}
PS C:\Users\pmacyszyn_adm\Documents\python\python> 
'''