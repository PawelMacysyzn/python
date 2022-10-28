class Cake:

    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit',
                   'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):

        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print("Gluten free: {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-'*20)

    @property
    def Text(self):
        return self.__text

    @Text.setter
    def Text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', [
              'chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolade Muffin', 'muffin',
              'chocolade', ['chocolade'], '', False, '')
cake03 = Cake('Super Sweet Maringue', 'meringue',
              'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa',
              [], 'cocoa', False, 'Good luck!')


print("Today in our offer:")
# for c in Cake.bakery_offer:
#     c.show_info()

# or

[c.show_info() for c in Cake.bakery_offer]   


'''
>>>>>Text can be set only for cake (Cocoa waffle)
Today in our offer:
VANILLA CAKE
Kind:        cake
Taste:       vanilla
Additives:
                chocolade
                nuts
Filling:     cream
Gluten free: False
Text:      Happy Birthday Margaret!
--------------------
CHOCOLADE MUFFIN
Kind:        muffin
Taste:       chocolade
Additives:
                chocolade
Gluten free: False
--------------------
SUPER SWEET MARINGUE
Kind:        meringue
Taste:       very sweet
Gluten free: True
--------------------
COCOA WAFFLE
Kind:        other
Taste:       cocoa
Filling:     cocoa
Gluten free: False
--------------------
'''
cake01.Text = 'Happy birthday!'
cake02.Text = '18'


[c.show_info() for c in Cake.bakery_offer]   
'''
>>>>>Text can be set only for cake (Cocoa waffle)
>>>>>Text can be set only for cake (Chocolade Muffin)
VANILLA CAKE
Kind:        cake
Taste:       vanilla
Additives:
                chocolade
                nuts
Filling:     cream
Gluten free: False
Text:      Happy birthday!
--------------------
CHOCOLADE MUFFIN
Kind:        muffin
Taste:       chocolade
Additives:
                chocolade
Gluten free: False
--------------------
SUPER SWEET MARINGUE
Kind:        meringue
Taste:       very sweet
Gluten free: True
--------------------
COCOA WAFFLE
Kind:        other
Taste:       cocoa
Filling:     cocoa
Gluten free: False
--------------------
'''