import csv
import types


def exportToFile_Static(path, header, data):
    with open(path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)
    # just to see that the function was indeed called
    print('>>> This is function exportToFile - static method')


def exportToFile_Class(cls, path):
    with open(path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand', 'model', 'IsOnSale'])
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])
    # just to see that the function was indeed called
    print('>>> This is function exportToFile - Class method')


def exportToFile_Instance(self, path):
    with open(path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand', 'model', 'IsOnSale'])
        writer.writerow([self.brand, self.model, self.IsOnSale])
    # just to see that the function was indeed called
    print('>>> This is function exportToFile - Instance method')


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

    def IsDamaged(self): return not (
        self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

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


car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)


'''
print('ExportToFile_Static' in dir(car_01))  # False
print('exportToFile_Static' in dir(car_01))  # False

print('ExportToFile_Static' in dir(Car))  # False
print('exportToFile_Static' in dir(Car))  # False
'''

print('Static-------'*10)
exportToFile_Static(r'C:\temp\export_static.csv', ['Brand', 'Model', 'IsOnSale'], [
                    car_01.brand, car_01.model, car_01.IsOnSale])
# >>> This is function exportToFile - static method

Car.ExportToFile_Static = exportToFile_Static                    
# >>> This is function exportToFile - static method
Car.ExportToFile_Static(r'C:\temp\export_static.csv', [
                        'Brand', 'Model', 'IsOnSale'], [car_01.brand, car_01.model, car_01.IsOnSale])


'''
print('ExportToFile_Static' in dir(Car))  # True
print('exportToFile_Static' in dir(Car))  # False

print('ExportToFile_Static' in dir(car_01))  # True
print('exportToFile_Static' in dir(car_01))  # False
'''


print('Class-------'*10)
Car.ExportToFile_Class = types.MethodType(exportToFile_Class, Car)
Car.ExportToFile_Class(path=r'C:\temp\export_Class.csv')


print('Instance-------'*10)
car_01.ExportToFile_Instance = types.MethodType(exportToFile_Instance, car_01)
car_01.ExportToFile_Instance(path=r'C:\temp\export_Instance.csv')

# ['ExportToFile_Class', 'ExportToFile_Instance', 'ExportToFile_Static',  ...
print(dir(car_01))

print(dir(Car))  # ['ExportToFile_Class', 'ExportToFile_Static', ...


print('-'*55)
# print('ExportToFile_Static' in dir(car_01))
# ...
# beter option is:

if hasattr(car_01, 'ExportToFile_Static') and callable(car_01.ExportToFile_Static):
    print('The object has method ExportToFile_Static')
if hasattr(car_01, 'ExportToFile_Class') and callable(car_01.ExportToFile_Class):
    print('The object has method ExportToFile_Class')
if hasattr(car_01, 'ExportToFile_Instance') and callable(car_01.ExportToFile_Instance):
    print('The object has method ExportToFile_Instance')

'''
The object has method ExportToFile_Static
The object has method ExportToFile_Class
The object has method ExportToFile_Instance
'''
