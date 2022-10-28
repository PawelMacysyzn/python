class MemoryClass:

    def __init__(self, list):
        self.list_of_items = list

    def __call__(self, item):
        self.list_of_items.append(item)


mem = MemoryClass([])
print("List of items in memory", mem.list_of_items)

mem.list_of_items.append('buy sugar')
print("List of items in memory", mem.list_of_items)

# This class is callable: True
print("This class is callable:", callable(MemoryClass))
'''
    def __call__(self, item):
        self.list_of_items.apped(item)

before:

print("This class is callable:", callable(mem)) # This class is callable: False

after adding def __call__(self, item):
print("This class is callable:", callable(mem)) # This class is callable: True
'''

mem('buy milk')
# List of items in memory ['buy sugar', 'buy milk']
print("List of items in memory", mem.list_of_items)
mem('buy coffe')
# List of items in memory ['buy sugar', 'buy milk', 'buy coffe']
print("List of items in memory", mem.list_of_items)
