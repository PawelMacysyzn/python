'''
recipe1
Stuffed Shells

TOTAL TIME
95 mins

SERVINGS
6 to 8 servings

Ingredients
2 tablespoons olive oil
3 garlic cloves, thinly sliced
1 (28-ounce) can whole, peeled tomatoes, crushed in a bowl
1/2 teaspoon salt
1-2 pinches sugar (optional)
2 cups (16 ounces) fresh whole or skim-milk ricotta
2 cups (8 ounces) grated mozzarella, divided
1 cup (4 ounces) finely grated Parmesan, divided
1 large egg
Finely grated zest of 1 lemon (about 1 tablespoon)
1/4 cup chopped parsley
1/4 teaspoon salt, plus more for the pasta water
1/8 teaspoon freshly ground black pepper
8 ounces jumbo shells (save the remaining shells for another use)
Torn basil leaves (about 2 sprigs) or 2 tablespoons chopped parsley (for garnish)
'''

'''
recipe2
Spaghetti Aglio e Olio (Pasta With Garlic and Oil)

TOTAL TIME
21 mins

SERVINGS
4 to 5 servings

Ingredients
1 teaspoon kosher salt, plus more for the pasta water
1 pound dried spaghetti
1/3 cup extra-virgin olive oil
4 large cloves garlic, peeled and very thinly sliced
1/2 teaspoon crushed red pepper flakes
1/2 cup finely grated Parmesan cheese, plus more to pass at the table
2 tablespoons finely chopped Italian parsley (optional)
'''

'''
recipe3
Matar Paneer

TOTAL TIME
30 mins

SERVINGS
4 servings

Ingredients
1 cup (8 ounces) canned whole peeled tomatoes
3 tablespoons canola oil, divided
1 tablespoon ginger, peeled and minced (from about a 1-inch piece)
2 cloves garlic, minced
1 small red onion, diced
2 whole cardamom pods
2 cloves whole
1 teaspoon garam masala
1/4 teaspoon mild chili powder, such as Kashmiri chili powder
1/2 teaspoon ground coriander
1/2 teaspoon ground cumin
1/2 teaspoon kosher salt, plus more to taste
1 cup water, plus more if needed
2 teaspoons maple syrup
2 tablespoons heavy cream
3/4 cup (4 ounces) frozen peas
8 ounces paneer, cut into 3/4-inch cubes
1/2 teaspoon dried fenugreek
1/4 cup loosely packed fresh cilantro, chopped
'''




import os
class Food:

    def __init__(self, recipe_name: str) -> None:
        self.name = self.get_name_of_recipe(recipe_name)
        self.kind = self.get_kind_of_recipe(recipe_name)
        self.total_time = self.get_total_time(recipe_name)
        self.servings = self.get_servings(recipe_name)
        self.ingredients = self.get_ingredients(recipe_name)

    def show(self):
        print('{} ({})'.format(self.name, self.kind))
        print('Preparation time: {} / {}'.format(self.total_time, self.servings))
        print('Ingredients: ({} items)'.format(len(self.ingredients)))
        for e, i in enumerate(self.ingredients):
            print('({:<2}) - {}'.format(e+1, i))


    @classmethod
    def open_ingredients(cls, recipe) -> str:
        with open(os.path.abspath(__file__), 'r') as file:
            in_line = False  # for test
            in_case = False  # for test
            for line in file:
                if line.upper().find("'''".upper()) != -1:
                    if in_line and in_case:
                        return StopIteration
                    else:
                        in_line = True

                if in_line and line.upper().find(recipe.upper()) != -1:
                    in_case = True

                if in_line and in_case:
                    if line != '\n':
                        yield line

    @classmethod
    def get_list_of_recip(cls, recipe: str) -> list:
        selected_recip = list()
        for line in cls.open_ingredients(recipe):
            selected_recip.append(line.rstrip('\n'))
        return selected_recip

    @classmethod
    def get_ingredients(cls, recipe: str) -> list:
        list_of_recip = cls.get_list_of_recip(recipe)
        filter_object = list(
            filter(lambda a: 'Ingredients' in a, list_of_recip))
        if len(filter_object) == 1:
            return list_of_recip[list_of_recip.index(*filter_object)+1:]

    @classmethod
    def get_get_item(cls, item: str, recipe: str):
        list_of_recip = cls.get_list_of_recip(recipe)
        filter_object = list(filter(lambda a: item in a, list_of_recip))
        if len(filter_object) == 1:
            return list_of_recip[list_of_recip.index(*filter_object)+1]

    @classmethod
    def get_name_of_recipe(cls, recipe: str) -> str:
        return cls.get_get_item('recipe', recipe)

    @classmethod
    def get_total_time(cls, recipe: str) -> str:
        return cls.get_get_item('TOTAL TIME', recipe)

    @classmethod
    def get_servings(cls, recipe: str) -> str:
        return cls.get_get_item('SERVINGS', recipe)

    @classmethod
    def get_kind_of_recipe(cls, recipe: str) -> str:
        list_of_kind = ['pasta', 'different']
        for kind in list_of_kind:
            if kind.upper() in cls.get_name_of_recipe(recipe).upper():
                return kind.capitalize()
            else:
                return list_of_kind[-1].capitalize()


def main():
    recipe_1 = Food('recipe1')
    var_1 = 0
    var_2 = 1

    # print([k for k, v in locals().items() if k == 'var_1'][0])
    recipe_1.show()
    pass


if __name__ == '__main__':
    main()
