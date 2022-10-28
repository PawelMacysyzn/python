import types
from unicodedata import name


def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(
            obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)


def export_all_cakes_to_html(cls, path):

    template_header = """
<table border=1>"""
    template = """
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>"""
    template_footer = """</indent>
</table>"""
    with open(path, "w") as f:
        f.write(template_header)
        for obj in cls.bakery_offer:
            content = template.format(
                obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
            f.write(content)
        f.write(template_footer)


def export_this_cake_to_html(self, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(
            self.name, self.kind, self.taste, self.additives, self.filling)
        f.write(content)


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


# static method:
Cake.export_1_cake_to_html = export_1_cake_to_html
Cake.export_1_cake_to_html(cake01, 'c:/temp/static_cake01.html')

print(callable(Cake.export_1_cake_to_html))  # True
print(callable(cake01.export_1_cake_to_html))  # True

# class method:
Cake.export_all_cakes_to_html = types.MethodType(
    export_all_cakes_to_html, Cake)
Cake.export_all_cakes_to_html('c:/temp/all_in_one_class_Cake.html')


# Instance method:
for cake in Cake.bakery_offer:
    cake.export_this_cake_to_html = types.MethodType(export_this_cake_to_html, cake)
    cake.export_this_cake_to_html('c:/temp/{}_Instance.html'.format(cake.name.replace(' ','_')))


for cake in Cake.bakery_offer:
    print(callable(cake.export_1_cake_to_html))  # True


