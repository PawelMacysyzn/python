import pickle
import glob


class Cake():

    known_types = [
        'cake', 'muffin', 'meringue',
        'biscuit', 'eclair', 'christmas',
        'pretzel', 'other']

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text=''):

        self.name = name

        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = Cake.known_types[-1]

        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.__gluten_free = gluten_free

        if self.kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake, not on {}'.format(kind))
            print()

        Cake.bakery_offer.append(self)

    def show_info(self):
        print(
            '{}. - {}     [{}]'.format(Cake.bakery_offer.index(self), self.name.upper(), self))
        print('Kind:           {}'.format(self.kind))
        print('Taste:          {}'.format(self.taste))
        print('Additives:   ')
        for additive in self.additives:
            print('            {}'.format(additive))
        print('Filling:        {}'.format(self.filling))
        print('Is gluten free: {}'.format(self.__gluten_free))
        print('Text:           {}'.format(self.__text))
        print('-'*20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, *additives):
        for additive in additives:
            self.additives.append(additive)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        '''
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake, not on {}'.format(self.kind))
        '''
        # or

        self.__text = new_text if (self.kind in Cake.known_types[0]) else print(
            '>>>>>Text can be set only for cake, not on {}'.format(self.kind))

    Text = property(__get_text, __set_text, None,
                    'Documentation: Text on the cake')

    def save_to_file(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_obj = pickle.load(f)

        cls.bakery_offer.append(new_obj)
        return new_obj

    @classmethod
    def cake_show_info(cls):
        print('len<{}>'.format(len(Cake.bakery_offer)))
        [cake.show_info() for cake in cls.bakery_offer]

    @staticmethod
    def get_bakery_files(catalog):
        return glob.glob(catalog +'/*.bakery')


cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla',
               ['chocolade', 'nuts'], 'cream', True, 'Happy Birthday')
cake_02 = Cake('Chocolade Muffin', 'muffin',
               'chocolade', ['chocolade'], '', False)
cake_03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', False)
# cake_04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [],
#                'cocoa', False, 'Written in Python')


cake_01.save_to_file('c:/temp/cake01.bakery')

cake_05 = Cake.read_from_file('c:/temp/cake01.bakery')

# Cake.cake_show_info()

Cake.bakery_offer[-1].show_info()
'''
3. - VANILLA CAKE
Kind:           cake
Taste:          vanilla       
Additives:
            chocolade
            nuts
Filling:        cream
Is gluten free: True
Text:           Happy Birthday
--------------------
'''

print(Cake.get_bakery_files(r'c:/temp'))