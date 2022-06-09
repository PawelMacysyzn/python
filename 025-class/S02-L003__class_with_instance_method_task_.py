class Cake():

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling

    def show_info(self):
        print('{}'.format(self.name.upper()))
        print('Kind:    {}'.format(self.kind))
        print('Taste:   {}'.format(self.taste))
        print('Additives:   ')
        for additive in self.additives: print('    {}'.format(additive))
        print('Filling: {}'.format(self.filling))
        print('-'*20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, *additives):
        for additive in additives:
            self.additives.append(additive)
    


cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake_02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake_03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [''], '')



cake_01.show_info()
cake_01.set_filling('coko')
cake_01.show_info()
cake_01.add_additives('dirt', 'snow', 'spiders')
cake_01.show_info()



    


