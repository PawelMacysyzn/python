# py -m unittest -v task2__class_with_instance_unitest_.py
import unittest
import task2__class_with_instance_ as test_object


recipe1 = ['recipe1', 'Stuffed Shells', 'TOTAL TIME', '95 mins',
           'SERVINGS', '6 to 8 servings', 'Ingredients',
           '2 tablespoons olive oil', '3 garlic cloves, thinly sliced',
           '1 (28-ounce) can whole, peeled tomatoes, crushed in a bowl',
           '1/2 teaspoon salt', '1-2 pinches sugar (optional)',
           '2 cups (16 ounces) fresh whole or skim-milk ricotta',
           '2 cups (8 ounces) grated mozzarella, divided',
           '1 cup (4 ounces) finely grated Parmesan, divided',
           '1 large egg',
           'Finely grated zest of 1 lemon (about 1 tablespoon)',
           '1/4 cup chopped parsley',
           '1/4 teaspoon salt, plus more for the pasta water',
           '1/8 teaspoon freshly ground black pepper', '8 ounces jumbo shells (save the remaining shells for another use)', 'Torn basil leaves (about 2 sprigs) or 2 tablespoons chopped parsley (for garnish)']

recipe2 = ['recipe2', 'Spaghetti Aglio e Olio (Pasta With Garlic and Oil)',
           'TOTAL TIME', '21 mins', 'SERVINGS', '4 to 5 servings',
           'Ingredients', '1 teaspoon kosher salt, plus more for the pasta water',
           '1 pound dried spaghetti', '1/3 cup extra-virgin olive oil',
           '4 large cloves garlic, peeled and very thinly sliced',
           '1/2 teaspoon crushed red pepper flakes',
           '1/2 cup finely grated Parmesan cheese, plus more to pass at the table',
           '2 tablespoons finely chopped Italian parsley (optional)']


class Unittest(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_get_list_of_recip(self):
        self.assertEqual(recipe2, test_object.get_list_of_recip('recipe2'))

    def test_get_name_of_recip(self):
        self.assertEqual(recipe2[1], test_object.get_name_of_recipe('recipe2'))

    def test_get_kind_of_recipe1(self):
        self.assertEqual(
            'Different', test_object.get_kind_of_recipe('recipe1'))

    def test_get_kind_of_recipe2(self):
        self.assertEqual('Pasta', test_object.get_kind_of_recipe('recipe2'))

    def test_get_total_time_recipe2(self):
        self.assertEqual('21 mins', test_object.get_total_time('recipe2'))

    def test_get_total_time_recipe1(self):
        self.assertEqual('95 mins', test_object.get_total_time('recipe1'))
