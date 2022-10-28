class Cake():

    known_types = [
        'cake', 'muffin', 'meringue',
        'biscuit', 'eclair', 'christmas',
        'pretzel', 'other']

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name

        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = Cake.known_types[-1]

        self.taste = taste
        self.additives = additives
        self.filling = filling
        Cake.bakery_offer.append(self)

    def show_info(self):
        print('{}'.format(self.name.upper()))
        print('Kind:    {}'.format(self.kind))
        print('Taste:   {}'.format(self.taste))
        print('Additives:   ')
        for additive in self.additives:
            print('    {}'.format(additive))
        print('Filling: {}'.format(self.filling))
        print('-'*20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, *additives):
        for additive in additives:
            self.additives.append(additive)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla',
               ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa')


'''
print("Today in our offer:")
for cake in Cake.bakery_offer:
    cake.show_info()
'''
# same, but better xd

[cake.show_info() for cake in Cake.bakery_offer]




print(isinstance(cake01, Cake))
print(type(cake01) is Cake)

print(vars(Cake))
print(dir(Cake))

print(vars(cake01))
print(dir(cake01))