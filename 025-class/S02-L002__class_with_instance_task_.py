bakery_offer = []

class Cake():

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling


cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake_02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake_03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [''], '')

bakery_offer.append(cake_01)
bakery_offer.append(cake_02)
bakery_offer.append(cake_03)

for num, cake in enumerate(bakery_offer):
    print('{} - {}'.format(num, cake.name), end=' ')
    print("- ({}) main taste: {} with additives of {}, filled with {}".format(\
        cake.kind, cake.taste, cake.additives, cake.filling))


