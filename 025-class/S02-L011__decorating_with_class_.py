import random


class MemoryClass:

    list_of_already_selected_items = []

    def __init__(self, funct) -> None:
        print('>> this is init of MemoryClass')
        self.funct = funct

    def __call__(self, list):
        print('This is call of MemoryClas istance')
        items_not_selected = [i for i in list if i not in MemoryClass.list_of_already_selected_items]
        print('+-- selected only from a list of', items_not_selected)
        item = self.funct(items_not_selected)
        MemoryClass.list_of_already_selected_items.append(item)
        return item


cars = ['Opel', 'Toyota', 'Fiat', 'Ford', 'Renaut', 'Mercedes',
        'BMW', 'Peugot', 'Porshe', 'Audi', 'VW', 'Mazda']


@MemoryClass
def SelectTodayPromotion(list_of_cars):
    return random.choice(list_of_cars)

@MemoryClass
def SelectTodayShow(list_of_cars):
    return random.choice(list_of_cars)

@MemoryClass
def SelectFreeAccessories(list_of_cars):
    return random.choice(list_of_cars)


print("Promotion:", SelectTodayPromotion(cars))
print("Show:", SelectTodayShow(cars))
print("Free accessories:", SelectFreeAccessories(cars))
