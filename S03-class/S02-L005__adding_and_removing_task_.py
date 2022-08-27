class Cake():

    known_types = [
        'cake', 'muffin', 'meringue',
        'biscuit', 'eclair', 'christmas',
        'pretzel', 'other']

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free):

        self.name = name

        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = Cake.known_types[-1]

        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.__gluten_free = gluten_free
        Cake.bakery_offer.append(self)

    def show_info(self):
        print('{}'.format(self.name.upper()))
        print('Kind:           {}'.format(self.kind))
        print('Taste:          {}'.format(self.taste))
        print('Additives:   ')
        for additive in self.additives:
            print('            {}'.format(additive))
        print('Filling:        {}'.format(self.filling))
        print('Is gluten free: {}'.format(self.__gluten_free))
        print('-'*20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, *additives):
        for additive in additives:
            self.additives.append(additive)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla',
              ['chocolade', 'nuts'], 'cream', True)
cake02 = Cake('Chocolade Muffin', 'muffin',
              'chocolade', ['chocolade'], '', False)
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', False)
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False)


# [cake.show_info() for cake in Cake.bakery_offer]

cake03.show_info()
'''
SUPER SWEET MARINGUE
Kind:           meringue
Taste:          very sweet
Additives:
Filling:
Is gluten free: False
--------------------
'''
cake03.__gluten_free = True
cake03.show_info()
'''
SUPER SWEET MARINGUE
Kind:           meringue
Taste:          very sweet
Additives:
Filling:
Is gluten free: False
--------------------
'''
print(vars(cake03))
'''
{'name': 'Super Sweet Maringue', 'kind': 'meringue', 'taste': 'very sweet', 'additives': [], 'filling': '',
 '_Cake__gluten_free': False, '__gluten_free': True}
'''
setattr(cake03, '__gluten_free', False)

print(vars(cake03))

cake03._Cake__gluten_free = True
cake03.show_info()
'''
SUPER SWEET MARINGUE
Kind:           meringue
Taste:          very sweet
Additives:
Filling:
Is gluten free: True
--------------------
'''

print(vars(cake03))
del cake03.__gluten_free
print(vars(cake03))
setattr(cake03, 'New_attribute', True)
print(vars(cake03))
del cake03._Cake__gluten_free
del cake03.New_attribute
print(vars(cake03))
setattr(cake03, '_Cake__gluten_free', False)
print(vars(cake03))

cake03.show_info()
'''
SUPER SWEET MARINGUE
Kind:           meringue
Taste:          very sweet
Additives:
Filling:
Is gluten free: False
--------------------
'''