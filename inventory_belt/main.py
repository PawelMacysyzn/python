# A program to select a tool from the inventory bar in the most optimal way
import random
import time
from typing import List
from plot import do_plot


class GraphicInventoryBar:

    @staticmethod
    def show_animation_in_console(start: int, target: int, size: int) -> None:
        '''
        Show an animation of thru around the inventory on the console

        start: int  -> The starting point, it cannot be the same as the ending point
        target: int -> End point
        size: int   -> Size of inventory
        '''

        way_value, list = InventoryBar.optimal_way_and_list(
            start, target, size)

        print('-'*55)
        print(*list)

        GraphicInventoryBar.method_orgin_for_console(start, way_value, list)

    @staticmethod
    def show_animation_in_plot(start: int, target: int, size: int) -> None:
        '''
        Show an animation of thru around the inventory on the plot

        start: int  -> The starting point, it cannot be the same as the ending point
        target: int -> End point
        size: int   -> Size of inventory
        '''

        way_value, list = InventoryBar.optimal_way_and_list(
            start, target, size)

        do_plot(list)
        print(list)

        GraphicInventoryBar.method_orgin_for_plot(start, way_value, list)

    @staticmethod
    def method_orgin_for_console(start: int, way_value: int, list: List[str]):

        if way_value > 0:
            direction = 1
            pointer = '->'
        elif way_value < 0:
            direction = -1
            pointer = '<-'

        for _ in range(abs(way_value)):
            time.sleep(1)
            list, next = GraphicInventoryBar.method_for_step(
                start, direction, list)
            start = next
            print(*list, pointer)

    @staticmethod
    def method_orgin_for_plot(start: int, way_value: int, list: List[str]):

        if way_value > 0:
            direction = 1
        elif way_value < 0:
            direction = -1

        for _ in range(abs(way_value)):
            list, next = GraphicInventoryBar.method_for_step(
                start, direction, list)
            start = next
            do_plot(list)

    @staticmethod
    def method_for_step(start: int, step_value: int, list: List[str]) -> tuple:

        last_index = len(list) - 1

        # Convert a pointer to a number
        list[start] = f"[{list.index('[_]')}]"

        next = start + step_value

        if next < 0:
            next = last_index
        elif next > last_index:
            next = 0

        # Convert a pointer to a number
        list[next] = '[_]'

        return list, next


class InventoryBar:

    @staticmethod
    def optimal_way(start: int, target: int, size: int) -> int:
        '''
        Returns way_value where sign is the direction and value is the number of pots to go

        start: int  -> The starting point, it cannot be the same as the ending point
        target: int -> End point
        size: int   -> Size of inventory
        '''
        return InventoryBar.optimal_way_and_list(start, target, size)[0]

    @staticmethod
    def optimal_way_and_list(start: int, target: int, size: int) -> tuple:
        '''
        Returns List[str] and way_value where sign is the direction and value is the number of pots to go

        start: int  -> The starting point, it cannot be the same as the ending point
        target: int -> End point
        size: int   -> Size of inventory
        '''
        list = Dummy_Inventory.dummy_list_inventory(size)

        if start == target:
            raise Exception(
                "Sorry, the destination cannot be the same as the starting point")

        list[start] = "[_]"
        list[target] = "[x]"

        way_name, way_value, start, target = InventoryBar.calculate_optimal_way(
            list)

        return way_value, list

    @staticmethod
    def show_optimal_way_from_random(size: int) -> None:
        '''
        Generates a graphical representation of the bar in the console, with random start and target parameters

        size: int   -> Size of inventory
        '''
        list = Dummy_Inventory.dummy_random_generate_inventory(size)
        way_name, way_value, start, target = InventoryBar.calculate_optimal_way(
            list)
        print(*list, f'-> {way_name}, {abs(way_value)}')
        print(
            f"{len(list)} elem, start {start}, target {target}  ({target}-{start}) -> {way_value}")

    @staticmethod
    def calculate_optimal_way(list: List[str]) -> tuple:
        '''
        # Return:
        way_name  : str  -> ('both', 'right', 'left')
        way_value : int
        start     : int  -> list.index("[_]")
        target    : int  -> list.index("[x]")
        '''

        bar_len = len(list)
        start = list.index("[_]")
        target = list.index("[x]")

        way_value = target - start
        way_name = None

        if abs(way_value) > bar_len/2:

            if way_value > 0:
                way_value = abs(way_value) - bar_len
            else:
                way_value = way_value + bar_len

        if abs(way_value) == bar_len/2:
            way_name = 'both'
        else:
            if way_value > 0:
                way_name = 'right'
            elif way_value < 0:
                way_name = 'left'
            else:
                raise Exception("Sorry, no move")

        return way_name, way_value, start, target


class Dummy_Inventory:
    """
    Static class with methods  
    """

    @staticmethod
    def show_dummy_inventory(repeat: int, size: int) -> None:
        '''
        # Show randomly generates inventory with numbers starting from 0 to (size-1) \n
        # With a random start "_" and target "x" field

        repeat: int -> how many times
        size: int   -> list, starting from 0 to (size-1)
        '''

        for _ in range(repeat):
            print(*Dummy_Inventory.dummy_random_generate_inventory(size))

    @staticmethod
    def dummy_random_generate_inventory(size: int) -> str:
        '''
        Randomly generates inventory with numbers starting from 0 to (size-1) \n
        With a random start "_" and target "x" field
        '''
        list_inventory = Dummy_Inventory.dummy_list_inventory(size)
        start, target = Dummy_Inventory.dummy_random_choice_for_start_and_target(
            list_inventory)

        # replace: start, target
        list_inventory = list(
            map(lambda x: x.replace(start, "[_]"), list_inventory))
        return list(map(lambda x: x.replace(target, "[x]"), list_inventory))

    @staticmethod
    def dummy_random_choice_for_start_and_target(list: List[str]) -> tuple:
        '''
        Randomly generate two non-repeating items from a list
        '''
        list = list.copy()
        start = random.choice(list)
        list.remove(start)
        target = random.choice(list)
        return start, target

    @staticmethod
    def dummy_list_inventory(size: int) -> List[str]:
        '''
        Return list, starting from 0 to (size-1)
        '''
        return [f"[{i}]" for i in range(size)]


'''
[x] [_] -> both, 1
2 elem, start 1, target 0  (0-1) -> -1

[x] [_] -> both, 1
2 elem, start 1, target 0  (0-1) -> -1

[x] [_] -> both, 1
2 elem, start 1, target 0  (0-1) -> -1

[_] [x] -> both, 1
2 elem, start 0, target 1  (1-0) -> 1

[_] [x] -> both, 1
2 elem, start 0, target 1  (1-0) -> 1

[_] [x] -> both, 1
2 elem, start 0, target 1  (1-0) -> 1

[0] [_] [x] -> right, 1
3 elem, start 1, target 2  (2-1) -> 1

[0] [_] [x] -> right, 1
3 elem, start 1, target 2  (2-1) -> 1

[0] [x] [_] -> left, 1
3 elem, start 2, target 1  (1-2) -> -1

[x] [_] [2] -> left, 1
3 elem, start 1, target 0  (0-1) -> -1

[_] [1] [x] -> left, 1
3 elem, start 0, target 2  (2-0) -> -1

[_] [1] [2] [x] [4] -> left, 2
5 elem, start 0, target 3  (3-0) -> -2

[x] [1] [2] [3] [_] -> right, 1
5 elem, start 4, target 0  (0-4) -> 1

[_] [1] [2] [3] [x] -> left, 1
5 elem, start 0, target 4  (4-0) -> -1

[0] [1] [_] [x] [4] -> right, 1
5 elem, start 2, target 3  (3-2) -> 1

[_] [1] [2] [3] [x] -> left, 1
5 elem, start 0, target 4  (4-0) -> -1

[0] [x] [2] [3] [4] [_] -> right, 2
6 elem, start 5, target 1  (1-5) -> 2

[_] [x] [2] [3] [4] [5] -> right, 1
6 elem, start 0, target 1  (1-0) -> 1

[_] [1] [2] [3] [4] [x] -> left, 1
6 elem, start 0, target 5  (5-0) -> -1

[0] [_] [2] [3] [4] [x] -> left, 2
6 elem, start 1, target 5  (5-1) -> -2

[0] [1] [2] [x] [4] [_] [6] -> left, 2
7 elem, start 5, target 3  (3-5) -> -2

[_] [1] [2] [3] [4] [5] [x] -> left, 1
7 elem, start 0, target 6  (6-0) -> -1

[0] [1] [2] [3] [_] [x] [6] -> right, 1
7 elem, start 4, target 5  (5-4) -> 1

[x] [_] [2] [3] [4] [5] [6] -> left, 1
7 elem, start 1, target 0  (0-1) -> -1

[0] [1] [x] [3] [4] [5] [_] -> right, 3
7 elem, start 6, target 2  (2-6) -> 3

[x] [1] [2] [3] [_] [5] [6] -> right, 3
7 elem, start 4, target 0  (0-4) -> 3

[x] [1] [2] [_] [4] [5] [6] -> left, 3
7 elem, start 3, target 0  (0-3) -> -3

[x] [1] [2] [3] [4] [5] [_] -> right, 1
7 elem, start 6, target 0  (0-6) -> 1

[0] [1] [2] [3] [x] [5] [_] -> left, 2
7 elem, start 6, target 4  (4-6) -> -2

[0] [1] [_] [3] [4] [5] [6] [7] [x] [9] -> left, 4
10 elem, start 2, target 8  (8-2) -> -4

[x] [1] [2] [3] [4] [5] [6] [7] [8] [_] -> right, 1
10 elem, start 9, target 0  (0-9) -> 1

[x] [1] [2] [3] [4] [5] [_] [7] [8] [9] -> right, 4
10 elem, start 6, target 0  (0-6) -> 4

[_] [1] [2] [3] [4] [5] [6] [7] [8] [x] -> left, 1
10 elem, start 0, target 9  (9-0) -> -1

[x] [1] [2] [3] [4] [5] [_] [7] [8] [9] [10] -> right, 5
11 elem, start 6, target 0  (0-6) -> 5

[0] [1] [2] [3] [4] [5] [6] [7] [8] [x] [_] -> left, 1
11 elem, start 10, target 9  (9-10) -> -1

[_] [1] [2] [3] [4] [5] [6] [7] [8] [x] [10] -> left, 2
11 elem, start 0, target 9  (9-0) -> -2

[x] [1] [2] [3] [4] [5] [6] [7] [8] [_] [10] -> right, 2
11 elem, start 9, target 0  (0-9) -> 2

[x] [1] [2] [3] [4] [5] [6] [7] [8] [9] [_] -> right, 1
11 elem, start 10, target 0  (0-10) -> 1

[_] [1] [2] [3] [4] [5] [6] [7] [8] [9] [x] -> left, 1
11 elem, start 0, target 10  (10-0) -> -1
'''

'''
Fault

-None-
'''


# for _ in range(1000):
#     InventoryBar.show_optimal_way_from_random(
#         Dummy_Inventory.dummy_random_generate_inventory(11))
#     print()


# # [_] [1] [2] [3] [4] [5] [6] [7] [8] [9] [x] -> left, 1
# print(InventoryBar.optimal_way(0, 10, 11))


# GraphicInventoryBar.show_animation_in_console(0, 8, 11)
'''
[_] [1] [2] [3] [4] [5] [6] [7] [x] [9] [10]
[0] [1] [2] [3] [4] [5] [6] [7] [x] [9] [_] <-
[0] [1] [2] [3] [4] [5] [6] [7] [x] [_] [10] <-
[0] [1] [2] [3] [4] [5] [6] [7] [_] [9] [10] <-
'''

# GraphicInventoryBar.show_animation_in_console(2, 8, 11)
'''
[0] [1] [_] [3] [4] [5] [6] [7] [x] [9] [10]
[0] [_] [2] [3] [4] [5] [6] [7] [x] [9] [10] <-
[_] [1] [2] [3] [4] [5] [6] [7] [x] [9] [10] <-
[0] [1] [2] [3] [4] [5] [6] [7] [x] [9] [_] <-
[0] [1] [2] [3] [4] [5] [6] [7] [x] [_] [10] <-
[0] [1] [2] [3] [4] [5] [6] [7] [_] [9] [10] <-
'''

# GraphicInventoryBar.show_animation_in_console(2, 7, 10)
'''
[0] [1] [_] [3] [4] [5] [6] [x] [8] [9]
[0] [1] [2] [_] [4] [5] [6] [x] [8] [9] ->
[0] [1] [2] [3] [_] [5] [6] [x] [8] [9] ->
[0] [1] [2] [3] [4] [_] [6] [x] [8] [9] ->
[0] [1] [2] [3] [4] [5] [_] [x] [8] [9] ->
[0] [1] [2] [3] [4] [5] [6] [_] [8] [9] ->
'''

# showing animation
# GraphicInventoryBar.show_animation_in_plot(0, 8, 11)
GraphicInventoryBar.show_animation_in_plot(2, 7, 10)