'''
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
    def __init__(self, name, kind, total_time, servings, ingredients) -> None:
        self.name = name
        self.kind = kind
        self.total_time = total_time
        self.servings = servings
        self.ingredients = ingredients.copy()


def open_ingredients():
    with open(os.path.abspath(__file__), 'r') as file:
        for nr, line in enumerate(file):
            if line.upper().find('ingredients'.upper()) != -1:
                print(nr+1,'Yep')
            if line.upper().find('class'.upper()) != -1:
                return 'End'
            print(line, end='')
            


open_ingredients()