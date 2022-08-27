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
        print('{}'.format(self.name.upper()))
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

    Text = property(__get_text, __set_text, None, 'Documentation: Text on the cake')



cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla',
               ['chocolade', 'nuts'], 'cream', True, 'Happy Birthday')
cake_02 = Cake('Chocolade Muffin', 'muffin',
               'chocolade', ['chocolade'], '', False)
cake_03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', False)
cake_04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [],
               'cocoa', False, 'Written in Python')



for cake in Cake.bakery_offer:
    cake.show_info()

print('*'*44)

cake_01.Text = 'Amazing python'
cake_02.Text = '18' 

[cake.show_info() for cake in Cake.bakery_offer]
